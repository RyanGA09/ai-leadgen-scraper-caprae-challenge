# AI Leadgen Scraper Caprae Challenge

## 🕵️‍♂️ Lead Generation Scraper

A lead generation tool using **Selenium** and optionally **SerpAPI** to find company names, URLs, and emails from Google search results.

## 📦 Features

- Keyword-based Google search scraping (title, URL, email)
- Export results to CSV
- Optional Streamlit UI
- SerpAPI version included for faster scraping

## Project Folder Structure

```sh
caprae-scraper/
├── README.md
├── report.md                # Technical explanation 1 page
├── streamlit_app.py         # Simple UI display
├── scraper_selenium.py      # Scraper with Selenium (main)
├── scraper_serpapi.py       # Scraper with SerpAPI (optional)
├── leads.csv                # Output file
└── assets/
    └── walkthrough_script.txt

```

## 🚀 Setup Instructions

```bash
# Clone repository
pip install -r requirements.txt
```

### 1. For Selenium Version

```bash
python scraper_selenium.py
```

### 2. For Streamlit UI

```bash
streamlit run streamlit_app.py
```

### 3. For SerpAPI Version

Set your API key:

```bash
export SERPAPI_API_KEY=your_key_here
python scraper_serpapi.py
```

---

## 📄 Files Included

| File                   | Description                     |
| ---------------------- | ------------------------------- |
| scraper_selenium.py    | Main scraping using Selenium    |
| scraper_serpapi.py     | Optional scraper using SerpAPI  |
| streamlit_app.py       | Streamlit UI                    |
| leads.csv              | Output CSV (Selenium results)   |
| leads_serpapi.csv      | Output CSV (SerpAPI results)    |
| report.md              | Summary of task and leads found |
| walkthrough_script.txt | Script for demo recording       |

## 🧑‍💼 Task Context

Submitted as part of pre-work for **Caprae Capital** internship.

---

Built with ❤️ by Ryan Gading Abdullah
