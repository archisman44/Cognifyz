Data Visualization Tool
A Flask-based web application that visualizes book price data from books_data.csv (sourced from books.toscrape.com) using interactive Plotly charts. The tool displays a histogram of price distribution, a bar chart of the top 10 most expensive books, and a scatter plot of all book prices with hover details.
Features

Loads book data (title and price) from books_data.csv (~1000 books).
Generates three interactive visualizations:
Histogram of book prices.
Bar chart of the top 10 most expensive books.
Scatter plot of book prices with hover details (title and price).


Ensures dataset has sufficient entries by re-scraping if needed.
Uses Plotly for interactivity (hover, zoom, pan).
Responsive design with Bootstrap and custom CSS.

Technologies

Backend: Flask, Python
Visualization: Plotly
Scraping: BeautifulSoup, Requests (for dataset generation)
Frontend: HTML, Bootstrap 5.3, JavaScript
Data Storage: CSV (via pandas)
Styling: Custom CSS

Prerequisites

Python 3.8+
Stable internet connection (for initial scraping if books_data.csv is missing or insufficient)

Installation

Clone the Repository:
git clone <repository-url>
cd Data-Visualization-Tool


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install flask pandas plotly requests beautifulsoup4


Project Structure:
Data-Visualization-Tool/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── books_data.csv (generated after first run)
└── README.md



Usage

Run the Application:
python app.py


The app starts on http://localhost:5000.
On first run, it scrapes ~1000 books from books.toscrape.com if books_data.csv is missing or has fewer than 500 books.


Access the Web Interface:

Open http://localhost:5000 in a browser.
View three interactive visualizations:
Histogram: Price distribution of all books.
Bar Chart: Top 10 most expensive books.
Scatter Plot: All book prices with hover details.


Interact with charts by hovering, zooming, or panning.


Check Logs:

Terminal logs show data loading and scraping progress (e.g., Loaded 1000 books from books_data.csv).
Useful for debugging if the dataset is incomplete.



Troubleshooting

"No data found" in Visualizations:

Cause: books_data.csv is empty or missing.
Fix: Delete books_data.csv and restart the app to force a scrape. Check terminal logs for errors (e.g., "Network error scraping page X").


Visualizations Not Displaying:

Cause: JavaScript or Plotly rendering issue.
Fix: Check browser console (F12) for errors. Ensure Plotly.js loaded correctly via CDN.


Only 20 Books in Visualizations:

Cause: books_data.csv contains only 20 books from a partial scrape.
Fix: Delete books_data.csv and restart the app. Verify books_data.csv has ~1000 rows:(Get-Content -Path .\books_data.csv | Measure-Object -Line).Lines




Network Errors During Scraping:

Cause: Connectivity issues or rate limiting by books.toscrape.com.
Fix: Increase time.sleep(1) to time.sleep(2) in app.py or check your internet connection.


Scrape Stops Early:

Cause: Site structure changed or pages inaccessible.
Fix: Verify http://books.toscrape.com/catalogue/page-2.html in a browser. Update base_url or selectors in app.py if needed.



Notes

The app scrapes up to 1000 books (50 pages × 20 books) from books.toscrape.com if needed.
Visualizations are interactive: hover to see details, click and drag to zoom, double-click to reset.
The scatter plot uses book index as the x-axis for simplicity; prices are on the y-axis.

Future Improvements

Add user input to select visualization types.
Include filters (e.g., price range, book category if available).
Support multiple datasets or upload functionality.
Add more advanced visualizations (e.g., box plots, heatmaps).

License
MIT License
