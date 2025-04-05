# scraper_serpapi.py
from serpapi import GoogleSearch
import csv
import os

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
        leads.append({"title": title, "url": link, "emails": []})

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
