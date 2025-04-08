# 🕵️‍♂️ AI Leadgen Scraper - Caprae Capital Challenge

A lead generation tool using **Selenium** to find company names, URLs, and emails from Google search results.

## 📦 Features

- Keyword-based Google search scraping (title, URL, email)
- Export results to CSV
- Streamlit UI for interaction
- Jupyter Notebook demo for step-by-step exploration

## 📁 Project Structure

```sh
caprae-scraper/
├── README.md
├── report.md # Technical explanation 1 page (Markdown)
├── report.pdf # Technical explanation 1 page (PDF)
├── streamlit_app_selenium.py # Web UI
├── scraper_selenium.py # Scraper with Selenium (Main)
├── scraper_selenium.ipynb # Scraper with Selenium (Demo)
├── leads_selenium.csv # Output file (Main)
└── demo_leads.csv.csv # Output file (Demo)
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

### Open Jupyter Notebook

```bash
jupyter notebook scraper_selenium.ipynb
```

---

## 📄 Files Included

| File                      | Description                          |
| ------------------------- | ------------------------------------ |
| scraper_selenium.py       | Scraper using Selenium               |
| streamlit_app_selenium.py | Streamlit interface                  |
| scraper_selenium.ipynb    | Jupyter Notebook demo (step-by-step) |
| leads.csv                 | Output CSV (Selenium results)        |
| report.md                 | Summary of task and leads found      |
| report.pdf                | Summary of task and leads found      |

**📓 The Jupyter Notebook version is useful for walking through the scraping and email extraction process interactively, and is aligned with the optional demo guideline.**

## 🧑‍💼 Task Context

Submitted as part of pre-work for **Caprae Capital** internship.

---

## LICENSE

[LICENSE](LICENSE)

Built with ❤️ by Ryan Gading Abdullah

&copy; 2025 Ryan Gading Abdullah. All rights reserved.
