# 📊 Data Visualization Tool

A **Flask-based web application** that visualizes book price data from `books_data.csv` (scraped from [books.toscrape.com](http://books.toscrape.com)) using **interactive Plotly charts**.  
It includes:

- 📉 A histogram of price distribution  
- 📊 A bar chart of the top 10 most expensive books  
- 🧮 A scatter plot of all book prices with hover details

---

## 🚀 Features

- Loads book data (title and price) from `books_data.csv` (~1000 books)
- Automatically scrapes data if dataset is missing or insufficient
- Generates **3 interactive visualizations** using Plotly:
  - **Histogram** of book prices
  - **Bar Chart** of top 10 most expensive books
  - **Scatter Plot** of all book prices with hover details
- Responsive frontend using **Bootstrap**
- Smooth interaction: hover, zoom, pan

---

## 🛠️ Technologies

| Layer        | Tech Stack                                |
|--------------|--------------------------------------------|
| **Backend**  | Flask, Python                              |
| **Frontend** | HTML, Bootstrap 5.3, JavaScript            |
| **Visualization** | Plotly                            |
| **Scraping** | BeautifulSoup, Requests                    |
| **Data**     | CSV file (`pandas`)                        |
| **Styling**  | Custom CSS                                 |

---

## ✅ Prerequisites

- Python 3.8+
- Stable internet connection (for initial data scraping)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Data-Visualization-Tool.git
cd Data-Visualization-Tool
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate:
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask pandas plotly requests beautifulsoup4
```

---

## 📁 Project Structure

```
Data-Visualization-Tool/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── books_data.csv          # Generated after first run
└── README.md
```

---

## ▶️ Usage

### Run the Application
```bash
python app.py
```

- Access: [http://localhost:5000](http://localhost:5000)
- On first run, scrapes ~1000 books if `books_data.csv` is missing or has < 500 rows.

### Visualizations
- 📉 **Histogram**: Price distribution
- 📊 **Bar Chart**: Top 10 most expensive books
- 🧮 **Scatter Plot**: All book prices with hover info

> 🖱️ Interact with charts: hover, zoom, pan, and reset.

---

## 🐞 Troubleshooting

### ❌ "No data found"
- **Cause:** `books_data.csv` is missing or empty  
- **Fix:** Delete the file and restart the app to trigger scraping

### ❌ Charts not displaying
- **Cause:** JavaScript/Plotly error  
- **Fix:** Open browser console (`F12`) and check for Plotly loading issues

### ❌ Only 20 books shown
- **Cause:** Incomplete scrape  
- **Fix:** Delete `books_data.csv` and rerun the app

### ❌ Network errors during scraping
- **Cause:** Site blocking or slow connection  
- **Fix:** Increase `time.sleep(1)` to `time.sleep(2)` in `app.py`

---

## 📝 Notes

- App scrapes up to **1000 books** (50 pages × 20 books) if needed
- Scatter plot uses **book index** as X-axis and **price** as Y-axis
- Visualizations are fully interactive using Plotly

---

## 🚧 Future Improvements

- Add dropdowns or filters (e.g., by price range or category)
- Upload support for custom CSVs
- More visualizations: Box plots, heatmaps, etc.
- Switch between light/dark themes

---

## 📄 License

[MIT License](LICENSE)
