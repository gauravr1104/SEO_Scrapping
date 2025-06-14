# SEO Scraping Tool

This project scrapes top website rankings from Google search results using Python, Selenium, BeautifulSoup, and undetected_chromedriver.

## 🚀 Features

- Headless scraping with Chrome
- Avoids detection using `undetected_chromedriver`
- Extracts top-ranked websites for any search query
- Saves data in a clean CSV format with Rank, Company, and Website

## 📁 Project Structure
SEO_Scrapping/
├── SEO Webscrapping/
│ ├── main.py # Main scraping script
│ └── companies.csv # Output data
├── README.md # Project description
└── requirements.txt # Dependencies

🧠 How It Works
Launches an undetected Chrome browser.

Sends a Google search request.

Parses the returned HTML using BeautifulSoup.

Extracts company names and URLs from result blocks.

Outputs data to a CSV.

📌 Requirements
Python 3.7+

Google Chrome installed

ChromeDriver (automatically handled by undetected_chromedriver)
