import pandas as pd
from flask import Flask, render_template
import plotly.express as px
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
import re
import time
import logging
import json

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to scrape books from books.toscrape.com (up to 1000)
def scrape_all_books_toscrape():
    books = []
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    page = 1
    max_pages = 50

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
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error scraping page {page}: {e}")
            break
        except Exception as e:
            logging.error(f"Unexpected error scraping page {page}: {e}")
            break

    if books:
        df = pd.DataFrame(books)
        df.to_csv("books_data.csv", index=False)
        logging.info(f"Saved {len(books)} books to books_data.csv")
    else:
        logging.warning("No books scraped.")
    return books

# Load and prepare the dataset
def load_data():
    try:
        df = pd.read_csv('books_data.csv')
        logging.info(f"Loaded {len(df)} books from books_data.csv")
        if len(df) < 500:
            logging.warning(f"Only {len(df)} books in CSV. Forcing re-scrape.")
            books = scrape_all_books_toscrape()
            df = pd.DataFrame(books)
    except FileNotFoundError:
        logging.info("books_data.csv not found. Scraping books...")
        books = scrape_all_books_toscrape()
        df = pd.DataFrame(books)
    
    if df.empty:
        logging.warning("No books available. Creating dummy data.")
        df = pd.DataFrame([{"Title": "No data found", "Price (£)": 0.0}])
    return df

@app.route('/')
def index():
    df = load_data()

    # Visualization 1: Histogram of book prices
    fig1 = px.histogram(
        df, x="Price (£)", nbins=30, title="Distribution of Book Prices",
        labels={"Price (£)": "Price (£)"},
        template="plotly_white"
    )
    fig1.update_layout(
        xaxis_title="Price (£)",
        yaxis_title="Number of Books",
        bargap=0.2
    )

    # Visualization 2: Bar chart of top 10 most expensive books
    top_10_expensive = df.nlargest(10, "Price (£)")
    fig2 = px.bar(
        top_10_expensive, x="Price (£)", y="Title", orientation='h',
        title="Top 10 Most Expensive Books",
        labels={"Price (£)": "Price (£)", "Title": "Book Title"},
        template="plotly_white"
    )
    fig2.update_layout(
        xaxis_title="Price (£)",
        yaxis_title="Book Title",
        height=400
    )

    # Visualization 3: Scatter plot of all books with hover details
    fig3 = px.scatter(
        df, x=df.index, y="Price (£)", hover_data=["Title"],
        title="Scatter Plot of Book Prices",
        labels={"Price (£)": "Price (£)", "index": "Book Index"},
        template="plotly_white"
    )
    fig3.update_traces(marker=dict(size=8))
    fig3.update_layout(
        xaxis_title="Book Index",
        yaxis_title="Price (£)"
    )

    # Convert Plotly figures to JSON for rendering in HTML
    graph1_json = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2_json = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3_json = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graph1_json=graph1_json, graph2_json=graph2_json, graph3_json=graph3_json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)