#  Vendr Scraper

##  Description

This project is a web scraper for [Vendr](https://www.vendr.com) using **Python** and **Selenium**. It extracts data on software products across three SaaS-related categories:

- DevOps
- IT Infrastructure
- Data Analytics and Management

Each parser collects:
- Product name
- Category
- Short description
- Median price
- Price range

Data is stored in a local SQLite database (`products.db`).

---

#  Project Structure

## vendr-scraper/
- ├── run_scraper.py  (Entry point)
- ├── products.db  (SQLite database (auto-generated))
- │
- ├── db/
- │ ├── database.py (DB connection and insert logic)
- │ └── test_db.py (Basic DB functionality tests)
- │
- ├── parsers/
- │ ├── devops_parser.py (DevOps category parser)
- │ ├── it_infrastructure_parser.py (IT Infrastructure parser)
- │ └── data_analytics_parser.py (Data Analytics parser)
- │
- └── README.md # This file

## Tech Stack

- Python 3
- Selenium
- SQLite (via sqlite3)
- ChromeDriver (managed with webdriver-manager)


## Branching
Each parser module is available on a separate branch for individual review:

- main — Complete scraper with all categories
- devops — DevOps parser only
- it-infrastructure — IT Infrastructure parser only
- data-analytics — Data Analytics parser only


##  How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt

Run the scraper:
python run_scraper.py

The script will:
Launch all 3 scrapers (DevOps, IT Infrastructure, Data Analytics)
Store the collected data in products.db
