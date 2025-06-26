import pandas as pd
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to scrape all books from books.toscrape.com (up to 1000)
def scrape_all_books_toscrape():
    books = []
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    page = 1
    max_pages = 50  # books.toscrape.com typically has ~1000 books across 50 pages

    while len(books) < 1000 and page <= max_pages:
        url = base_url.format(page)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            logging.debug(f"Scraping page {page}: {url}")
            response = requests.get(url, timeout=30, headers=headers)
            response.encoding = "utf-8"
            if response.status_code != 200:
                logging.warning(f"Page {page} returned status {response.status_code}. Stopping scrape.")
                break

            soup = BeautifulSoup(response.text, "html.parser")
            page_books = soup.find_all("article", class_="product_pod")
            if not page_books:
                logging.info(f"No books found on page {page}. Stopping scrape.")
                break

            for book in page_books:
                try:
                    title = book.h3.a["title"]
                    price = book.find("p", class_="price_color").text
                    price = float(re.sub(r'[^\d.]', '', price))
                    books.append({"Title": title, "Price (£)": price})
                except (AttributeError, ValueError) as e:
                    logging.error(f"Error processing book on page {page}: {e}")
                    continue

            logging.info(f"Scraped {len(page_books)} books from page {page}. Total books: {len(books)}")
            page += 1
            time.sleep(1)  # Rate limiting
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error scraping page {page}: {e}")
            break
        except Exception as e:
            logging.error(f"Unexpected error scraping page {page}: {e}")
            break

    # Save to CSV
    if books:
        df = pd.DataFrame(books)
        df.to_csv("books_data.csv", index=False)
        logging.info(f"Saved {len(books)} books to books_data.csv")
    else:
        logging.warning("No books scraped.")
    return books

def scrape_website(url):
    try:
        time.sleep(1)  # Rate limiting
        logging.debug(f"Scraping custom URL: {url}")

        if "goodreads.com" in url:
            options = Options()
            options.headless = True  # Fixed syntax error
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            driver.quit()

            books = []
            for item in soup.find_all("tr", itemprop="itemListElement"):
                try:
                    title_tag = item.find("a", class_="bookTitle")
                    price_tag = item.find("span", class_="price")
                    if title_tag:
                        title = title_tag.text.strip()
                        price = price_tag.text if price_tag else "N/A"
                        if price != "N/A":
                            price = float(re.sub(r'[^\d.]', '', price))
                        books.append({"Title": title, "Price (£)": price})
                except (AttributeError, ValueError) as e:
                    logging.error(f"Error processing Goodreads book: {e}")
                    continue
        else:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, timeout=30, headers=headers)
            response.encoding = "utf-8"
            if response.status_code != 200:
                logging.error(f"Failed to fetch {url}. Status: {response.status_code}")
                return [{"Title": "Error", "Price (£)": f"Failed to fetch webpage (Status: {response.status_code})"}]
            
            soup = BeautifulSoup(response.text, "html.parser")

            if "books.toscrape.com" in url:
                books = []
                for book in soup.find_all("article", class_="product_pod"):
                    try:
                        title = book.h3.a["title"]
                        price = book.find("p", class_="price_color").text
                        price = float(re.sub(r'[^\d.]', '', price))
                        books.append({"Title": title, "Price (£)": price})
                    except (AttributeError, ValueError) as e:
                        logging.error(f"Error processing book.toscrape.com book: {e}")
                        continue
            elif "quotes.toscrape.com" in url:
                books = []
                for quote in soup.find_all("div", class_="quote"):
                    try:
                        text = quote.find("span", class_="text").text.strip()
                        books.append({"Title": text, "Price (£)": "N/A"})
                    except AttributeError as e:
                        logging.error(f"Error processing quote: {e}")
                        continue
            elif "scrapethissite.com" in url:
                books = []
                for row in soup.find_all("tr", class_="team"):
                    try:
                        name = row.find("td", class_="name").text.strip()
                        books.append({"Title": name, "Price (£)": "N/A"})
                    except AttributeError as e:
                        logging.error(f"Error processing scrapethissite.com item: {e}")
                        continue
            else:
                books = []
                for item in soup.find_all("div", class_="s-result-item"):
                    try:
                        title_tag = item.find("span", class_="a-text-normal")
                        price_tag = item.find("span", class_="a-price")
                        if title_tag and price_tag:
                            title = title_tag.text.strip()
                            price = price_tag.find("span", class_="a-offscreen").text
                            price = float(re.sub(r'[^\d.]', '', price))
                            books.append({"Title": title, "Price (£)": price})
                    except (AttributeError, ValueError) as e:
                        logging.error(f"Error processing generic item: {e}")
                        continue
        
        if not books:
            logging.warning(f"No books found at {url}")
            return [{"Title": "No data", "Price (£)": "No books found on this page"}]
        logging.info(f"Scraped {len(books)} books from {url}")
        return books
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return [{"Title": "Error", "Price (£)": str(e)}]

@app.route('/')
def index():
    books = []
    try:
        df = pd.read_csv('books_data.csv')
        books = df.to_dict('records')
        logging.info(f"Loaded {len(books)} books from books_data.csv")
        # Force re-scrape if fewer than 500 books
        if len(books) < 500:
            logging.warning(f"Only {len(books)} books in CSV. Forcing re-scrape.")
            books = scrape_all_books_toscrape()
    except FileNotFoundError:
        logging.info("books_data.csv not found. Scraping books...")
        books = scrape_all_books_toscrape()

    if not books:
        books = [{"Title": "No data found", "Price (£)": "N/A"}]
        logging.warning("No books available. Using default empty data.")

    total_books = len(books)
    total_pages = (total_books + 49) // 50  # Ceiling division for 50 books per page
    logging.debug(f"Rendering index: page=1, total_books={total_books}, total_pages={total_pages}")
    return render_template('index.html', books=books[:50], page=1, total_pages=total_pages, total_books=total_books)

@app.route('/books', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))
    books = []
    try:
        df = pd.read_csv('books_data.csv')
        books = df.to_dict('records')
        logging.info(f"Loaded {len(books)} books from books_data.csv for page {page}")
        # Force re-scrape if fewer than 500 books
        if len(books) < 500:
            logging.warning(f"Only {len(books)} books in CSV. Forcing re-scrape.")
            books = scrape_all_books_toscrape()
    except FileNotFoundError:
        logging.info("books_data.csv not found. Scraping books...")
        books = scrape_all_books_toscrape()

    if not books:
        books = [{"Title": "No data found", "Price (£)": "N/A"}]
        logging.warning("No books available. Using default empty data.")

    total_books = len(books)
    total_pages = (total_books + 49) // 50  # Ceiling division for 50 books per page
    start = (page - 1) * 50
    end = start + 50
    paginated_books = books[start:end]
    logging.debug(f"Serving books for page {page}: start={start}, end={end}, books_returned={len(paginated_books)}")
    return jsonify({
        "books": paginated_books,
        "page": page,
        "total_pages": total_pages,
        "total_books": total_books
    })

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        logging.error("No URL provided in scrape request")
        return jsonify({"error": "No URL provided"}), 400
    books = scrape_website(url)
    logging.info(f"Returning {len(books)} books from scrape endpoint")
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)