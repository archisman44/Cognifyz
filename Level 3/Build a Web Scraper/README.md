# Book Scraper Web App

A Flask-based web application that scrapes book data (title and price) from `books.toscrape.com` (up to 1000 books), saves it to a CSV file, and displays it with pagination (50 books per page). Users can also scrape books from custom URLs (e.g., `books.toscrape.com`, `goodreads.com`, `quotes.toscrape.com`, `scrapethissite.com`) via a web interface.

## Features
- Scrapes up to 1000 books from `books.toscrape.com` and saves them to `books_data.csv`.
- Displays books in a paginated table (50 books per page) with "Next" and "Previous" buttons.
- Supports custom URL scraping through a web form, displaying results without pagination.
- Uses Bootstrap for responsive styling and custom CSS for enhanced visuals.
- Includes logging for debugging scraping and pagination issues.

## Technologies
- **Backend**: Flask, Python
- **Scraping**: BeautifulSoup, Requests, Selenium (for Goodreads)
- **Frontend**: HTML, Bootstrap 5.3, JavaScript
- **Data Storage**: CSV (via pandas)
- **Styling**: Custom CSS

## Prerequisites
- Python 3.8+
- Chrome browser and [ChromeDriver](https://chromedriver.chromium.org/) (for Goodreads scraping)
- Stable internet connection (for scraping)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Build-a-Web-Scraper
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install flask pandas requests beautifulsoup4 selenium
   ```

4. **Install ChromeDriver**:
   - Download ChromeDriver matching your Chrome browser version from [chromedriver.chromium.org](https://chromedriver.chromium.org/).
   - Add ChromeDriver to your system PATH or place it in the project directory and update `app.py`:
     ```python
     driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe', options=options)
     ```

5. **Project Structure**:
   ```
   Build-a-Web-Scraper/
   ├── app.py
   ├── templates/
   │   └── index.html
   ├── static/
   │   └── style.css
   ├── books_data.csv (generated after first run)
   └── README.md
   ```

## Usage
1. **Run the Application**:
   ```bash
   python app.py
   ```
   - The app starts on `http://localhost:5000`.
   - On first run, it scrapes ~1000 books from `books.toscrape.com` and saves them to `books_data.csv`.

2. **Access the Web Interface**:
   - Open `http://localhost:5000` in a browser.
   - The table displays the first 50 books with pagination controls ("Page 1 of 20 (Total Books: ~1000)").
   - Use "Next" and "Previous" buttons to navigate pages.
   - Enter a custom URL (e.g., `http://books.toscrape.com/`) in the form and click "Scrape" to fetch and display books from that URL (pagination is disabled for custom scraping).

3. **Check Logs**:
   - Terminal logs show scraping progress (e.g., `Scraped 20 books from page 1. Total books: 20`).
   - Logs are useful for debugging if fewer than 1000 books are scraped.

## Troubleshooting
- **"Page 1 of 1 (Total Books: 20)" Issue**:
  - **Cause**: `books_data.csv` contains only 20 books, likely from a partial scrape.
  - **Fix**: Delete `books_data.csv` and restart the app to force a full scrape. Check terminal logs for errors (e.g., "Network error scraping page X").
  - **Verify**: Ensure `books_data.csv` has ~1000 rows after scraping:
    ```powershell
    (Get-Content -Path .\books_data.csv | Measure-Object -Line).Lines
    ```

- **Pagination Buttons Not Working**:
  - **Cause**: Insufficient books in `books_data.csv` (e.g., only 20 books, so `total_pages = 1`).
  - **Fix**: Delete `books_data.csv` and re-run the app. Check browser console (F12) for JavaScript errors in the `fetch` call to `/books`.

- **Selenium Errors**:
  - **Cause**: ChromeDriver not found or version mismatch.
  - **Fix**: Ensure ChromeDriver is installed and matches your Chrome version. Update the path in `app.py` if needed.

- **Network Errors**:
  - **Cause**: Connectivity issues or rate limiting by `books.toscrape.com`.
  - **Fix**: Increase `time.sleep(1)` to `time.sleep(2)` in `scrape_all_books_toscrape` or check your internet connection.

- **Scrape Stops Early**:
  - **Cause**: Site structure changed or pages are inaccessible.
  - **Fix**: Verify `http://books.toscrape.com/catalogue/page-2.html` in a browser. Update `base_url` or BeautifulSoup selectors in `app.py` if needed.

## Notes
- The app scrapes up to 1000 books (50 pages × 20 books) from `books.toscrape.com`.
- If `books_data.csv` has fewer than 500 books, the app forces a re-scrape on startup.
- Goodreads scraping requires Selenium and may be slow due to headless browser usage.
- Custom URL scraping supports specific sites (`books.toscrape.com`, `quotes.toscrape.com`, `scrapethissite.com`, `goodreads.com`) and a generic Amazon-like scraper.

## Future Improvements
- Add caching for custom URL scraping results.
- Implement sorting and filtering for the book table.
- Support additional websites with dynamic scraping logic.
- Add error alerts in the UI for failed scrapes.

## License
MIT License