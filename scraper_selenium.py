# scraper_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import csv
import re


def extract_emails(text):
    # Simple regex to capture email-like patterns
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)


def search_leads(query, num_results=10):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("Searching for:", query)
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    results = []
    links = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf a")[:num_results]

    for link in links:
        url = link.get_attribute("href")
        title = link.text
        try:
            driver.execute_script("window.open(arguments[0]);", url)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            page_text = driver.find_element(By.TAG_NAME, "body").text
            emails = extract_emails(page_text)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            emails = []
            driver.switch_to.window(driver.window_handles[0])
        results.append({"title": title, "url": url, "emails": emails})

    driver.quit()
    return results


def save_to_csv(results, filename="leads.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "emails"])
        writer.writeheader()
        for row in results:
            row["emails"] = ", ".join(row["emails"])
            writer.writerow(row)


if __name__ == "__main__":
    query = input("Enter your lead generation keyword: ")
    leads = search_leads(query, num_results=5)
    save_to_csv(leads)
    print("Saved to leads.csv")
