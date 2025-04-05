# scraper_serpapi.py
from serpapi import GoogleSearch
import csv
import os
import requests
import re
import time

# Fungsi untuk ekstraksi email dari teks HTML
def extract_emails(text):
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(email_regex, text)

def search_leads_serpapi(query, num_results=10):
    api_key = os.getenv("SERPAPI_API_KEY")  # Set your API key in environment variable
    if not api_key:
        raise ValueError("Please set your SERPAPI_API_KEY environment variable.")

    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    leads = []
    for result in results.get("organic_results", []):
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet", "")

        # Coba ambil isi halaman dan ekstrak email
        emails = []
        try:
            print(f"Visiting {link}")
            response = requests.get(link, timeout=10)
            page_text = response.text
            emails = extract_emails(page_text)
        except Exception as e:
            print(f"Error visiting {link}: {e}")

        leads.append({
            "title": title,
            "url": link,
            "emails": list(set(emails))  # Hindari email duplikat
        })

        time.sleep(1)  # Hindari terlalu cepat saat request

    return leads

def save_to_csv(results, filename="leads_serpapi.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "emails"])
        writer.writeheader()
        for row in results:
            row["emails"] = ", ".join(row["emails"])
            writer.writerow(row)

if __name__ == "__main__":
    query = input("Enter your search keyword: ")
    leads = search_leads_serpapi(query, num_results=5)
    save_to_csv(leads)
    print("Saved to leads_serpapi.csv")
