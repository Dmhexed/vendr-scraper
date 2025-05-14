from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def parse_devops():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = "https://www.vendr.com/categories/devops"
    driver.get(url)
    time.sleep(5)

    # Scroll down to load cards
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    cards = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/marketplace/"]')
    unique_links = {}
    for card in cards:
        try:
            href = card.get_attribute("href")
            if href and href not in unique_links:
                unique_links[href] = True
        except:
            continue

    results = []

    for href in unique_links.keys():
        print(f"load link: {href}")
        try:
            driver.get(href)
            time.sleep(3)

            # name
            try:
                name_element = driver.find_element(By.TAG_NAME, "h1")
                name = name_element.text.strip()
            except:
                try:
                    name = driver.title.split(" | ")[0].strip()
                except:
                    name = "N/A"

            # about
            try:
                about_element = driver.find_element(By.CSS_SELECTOR, 'div._read-more-box__content_122o3_1 p')
                about = about_element.text.strip()
            except:
                about = "N/A"

            # Median
            try:
                median_element = driver.find_element(By.CSS_SELECTOR, 'div._rangeAverage_118fo_42')
                median = median_element.text.strip().replace("Median:", "").strip()
            except:
                median = "N/A"

            # price range
            try:
                price_low = driver.find_element(By.CSS_SELECTOR, '._rangeSlider_118fo_13 span.v-fw-600.v-fs-12:nth-child(1)').text.strip()
                price_high = driver.find_element(By.CSS_SELECTOR, '._rangeSlider_118fo_13 span.v-fw-600.v-fs-12:nth-child(3)').text.strip()
                price_range = f"{price_low} – {price_high}"
            except:
                price_range = "N/A"

            if all(x == "N/A" for x in [name, about, median, price_range]):
                continue

            results.append({
                "name": name,
                "category": "DevOps",
                "description": about,
                "median": median,
                "price_range": price_range
            })

        except Exception as e:
            print(f"Error while processing {href}: {e}")
            continue

    driver.quit()
    return results
