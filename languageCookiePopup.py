'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Start Chrome
driver = webdriver.Chrome()

# Open the page
driver.get("https://shop.sartorius.com/in/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors")

# Let the page fully load and render the shadow DOM
time.sleep(5)

try:
    # Step 1: Access the <aside> shadow host
    shadow_host = driver.find_element("css selector", "aside#usercentrics-cmp-ui")

    # Step 2: Get shadow root
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Step 3: Find the "Agree" button by ID
    agree_button = shadow_root.find_element("css selector", "button#accept")

    # Step 4: Click the button
    agree_button.click()

    print("✅ 'Agree' button clicked successfully.")
except Exception as e:
    print("❌ Failed to click 'Agree' button:", e)

'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://shop.sartorius.com/in/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors")

# Wait for the page to load
time.sleep(5)

def handle_cookie_and_language_popup(driver):
    wait = WebDriverWait(driver, 15)
    # ✅ Step 1: Accept cookies (inside Shadow DOM)
    try:
        shadow_host = driver.find_element("css selector", "aside#usercentrics-cmp-ui")
        shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        agree_button = shadow_root.find_element("css selector", "button#accept")
        agree_button.click()
        print("✅ Clicked Agree")
    except Exception as e:
        print("❌ Cookie popup failed:", e)

    # Wait for the language popup to appear
    time.sleep(5)

    # ✅ Step 2: Select country "us" and language "en"
    try:
        # Country dropdown
        country_select_elem = driver.find_element("css selector", "select[data-js-countryselect]")
        country_select = Select(country_select_elem)
        country_select.select_by_value("us")  # Select United States

        # Language dropdown
        language_select_elem = driver.find_element("css selector", "select[data-js-languageselect]")
        language_select = Select(language_select_elem)
        language_select.select_by_value("en")  # Select English

        print("✅ Selected country and language")

        # ✅ Step 3: Click Save button
        save_button = driver.find_element("css selector", "button[data-js-submit]")
        save_button.click()
        print("✅ Saved preferences")


    except Exception as e:
        print("❌ Language popup interaction failed:", e)

handle_cookie_and_language_popup(driver)

time.sleep(5)
def get_pdf_links(driver):
    try:
        # Wait for and click the Documents tab
        documents_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "documentsTabHeader"))
        )
        documents_tab.click()
        print("✅ Clicked on 'Documents' tab")
    except Exception as e:
        print("❌ Failed to click Documents tab:", e)
        return []

    # Give time for the content to load
    time.sleep(5)

    try:
        # Find all PDF links under product-download__title
        document_pdf_links = driver.find_elements(By.XPATH, '//div[@class="product-download__title"]//a[contains(@href, ".pdf")]')
        pdf_urls = [link.get_attribute("href") for link in document_pdf_links]
        print(f"✅ Found {len(pdf_urls)} PDF link(s).")
        return pdf_urls
    except Exception as e:
        print("❌ Error while extracting PDF links:", e)
        return []