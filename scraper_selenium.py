# scraper_selenium.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

def extract_emails(text):
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)

def search_leads(query, num_results=10):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    )

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("Searching for: ", query)
    driver.get("https://www.google.com")

    results = []
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        collected_links = set()
        page = 0

        while len(results) < num_results:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="tF2Cxc"]'))
            )
            search_results = driver.find_elements(By.XPATH, '//div[@class="tF2Cxc"]')

            for result in search_results:
                if len(results) >= num_results:
                    break

                try:
                    link_elem = result.find_element(By.XPATH, './/a')
                    url = link_elem.get_attribute("href")

                    if url in collected_links:
                        continue

                    collected_links.add(url)

                    title = "(No title)"
                    try:
                        title_elem = result.find_element(By.XPATH, './/h3')
                        if title_elem:
                            title = title_elem.text.strip()
                    except:
                        pass

                    print(f"Visiting: {title} ({url})")
                    driver.execute_script("window.open(arguments[0]);", url)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(3)

                    page_text = driver.page_source
                    emails = extract_emails(page_text)

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    results.append({
                        "title": title if title else "(No title)",
                        "url": url if url else "(No URL)",
                        "emails": emails if url else "(No emails)"
                    })
                except Exception as e:
                    print(f"Error accessing result: {e}")
                    try:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    except:
                        pass

            try:
                next_button = driver.find_element(By.ID, "pnnext")
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(2)
                next_button.click()
                page += 1
                time.sleep(3)
            except:
                print("No more pages.")
                break

    except Exception as e:
        print("Search failed:", e)

    driver.quit()
    return results

def save_to_csv(results, filename="leads_selenium.csv"):
    folder_path = "assets/data"
    os.makedirs(folder_path, exist_ok=True)  # Buat folder jika belum ada
    full_path = os.path.join(folder_path, filename)

    with open(full_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "emails"])
        writer.writeheader()
        for row in results:
            writer.writerow({
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "emails": ", ".join(row.get("emails", []))
            })

if __name__ == "__main__":
    query = input("Enter your lead generation keyword: ")
    leads = search_leads(query, num_results=7)
    if leads:
        save_to_csv(leads)
        print("Saved to assets/data/leads_selenium.csv")
    else:
        print("No leads found.")
