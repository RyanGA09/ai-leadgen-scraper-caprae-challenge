# 🕵️‍♂️ AI Leadgen Scraper - Caprae Capital Challenge

A lead generation tool using **Selenium** to find company names, URLs, and emails from Google search results.

## 📦 Features

- Keyword-based Google search scraping (title, URL, email)
- Export results to CSV
- Streamlit UI for interaction

## 📁 Project Structure

```sh
caprae-scraper/ 
├── README.md 
├── report.md # Technical explanation 1 page 
├── streamlit_app.py # Web UI 
├── scraper_selenium.py # Scraper with Selenium (main) 
├── leads.csv # Output file 
└── assets/ 
    └── walkthrough_script.txt
```

## 🚀 Setup Instructions

```bash
# Clone repository
pip install -r requirements.txt
```

### Run CLI version

```bash
python scraper_selenium.py
```

### Run Streamlit UI

```bash
streamlit run streamlit_app_selenium.py
```

---

## 📄 Files Included

| File                      | Description                     |
| ------------------------- | ------------------------------- |
| scraper_selenium.py       | Scraper using Selenium          |
| streamlit_app_selenium.py | Streamlit interface             |
| leads.csv                 | Output CSV (Selenium results)   |
| report.md                 | Summary of task and leads found |
| walkthrough_script.txt    | Script for demo recording       |

## 🧑‍💼 Task Context

Submitted as part of pre-work for **Caprae Capital** internship.

---

## LICENSE

[LICENSE](LICENSE)

Built with ❤️ by Ryan Gading Abdullah

&copy; 2025 Ryan Gading Abdullah. All rights reserved.
