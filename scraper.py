from playwright.sync_api import sync_playwright
import pandas as pd
import random
import re

MAX_PAGES = None   # ใส่ None ถ้าอยากดึงทั้งหมด
BASE_SEARCH_URL = "https://www.jobthai.com/jobsearch/computer-it"

programming_keywords = [
    "Python", "Java", "C#", "C++", "SQL",
    "JavaScript", "PHP", "Go", "Swift",
    "Kotlin", "R", "Ruby", "TypeScript",
    "VB.NET", ".NET", "Node.js"
]

results = []


def scroll_to_bottom(page):
    previous_height = 0
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1500)
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == previous_height:
            break
        previous_height = current_height


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context()
    page = context.new_page()

    # เข้า homepage ก่อนกัน block
    page.goto("https://www.jobthai.com/")
    page.wait_for_timeout(4000)

    page_number = 1

    while True:
        if MAX_PAGES is not None and page_number > MAX_PAGES:
            print("Reached MAX_PAGES limit.")
            break
        
        search_url = BASE_SEARCH_URL + '/' +str(page_number)
        print(f"\nScraping page {page_number}")

        page.goto(search_url)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)

        scroll_to_bottom(page)

        job_elements = page.locator("a[href*='/company/job/']").all()

        job_urls = []
        for job in job_elements:
            href = job.get_attribute("href")
            if href:
                if href.startswith("/"):
                    href = "https://www.jobthai.com" + href
                href = href.replace("/company/job/", "/job/")
                job_urls.append(href)

        job_urls = list(set(job_urls))

        if len(job_urls) == 0:
            print("No more jobs found. Stopping.")
            break

        print("Found jobs:", len(job_urls))

        for job_url in job_urls:
            try:
                page.goto(job_url)
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(random.randint(2000,4000))

                # ✅ ดึง company
                try:
                    company = page.locator("text=See more company details").first.locator("xpath=../../..").inner_text()
                    company = company.split("\n")[0]
                except:
                    company = "Unknown"

                # ✅ ดึง vacancies
                try:
                    vacancy_text = page.locator("text=Vacancies").locator("xpath=..").inner_text()
                    vacancy_match = re.search(r"\d+", vacancy_text)
                    vacancies = vacancy_match.group() if vacancy_match else "1"
                except:
                    vacancies = "1"
                
                # ✅ ดึง Job Title
                try:
                    job_title = page.locator("h1").first.inner_text().strip()
                except:
                    job_title = "Unknown"

                # ✅ ดึงวันที่
                try:
                    body_text = page.inner_text("body")
                    date_match = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s+\d{4}", body_text)
                    post_date = date_match.group() if date_match else "Unknown"
                except:
                    post_date = "Unknown"




                text = page.inner_text("body")

                found_languages = [
                    lang for lang in programming_keywords
                    if re.search(rf"\b{re.escape(lang)}\b", text, re.IGNORECASE)
                ]

                for lang in found_languages:
                    results.append({
                        "URL": job_url,
                        "Company": company.strip(),
                        "Vacancies": vacancies,
                        "Language": lang,
                        "Job Title": job_title,
                        "Date": post_date
                    })

                print("Done:", job_url)

                page.wait_for_timeout(random.randint(1500,3000))

            except Exception as e:
                print("Skipped:", job_url)

        page_number += 1

    browser.close()


df = pd.DataFrame(results)

# 🔥 กันไฟล์ทับ → append ถ้ามีไฟล์อยู่แล้ว
import os

file_name = "jobthai_programming_languages.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode="a", header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print("\nFinished scraping.")
print("Total rows collected:", len(df))