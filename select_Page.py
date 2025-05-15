from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# Wait for the page to load
time.sleep(5)

def handle_cookie_and_language_popup(url):

    driver.get(url)
    time.sleep(10)
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
    print(driver.current_url)
    time.sleep(5)
    
    cookies = driver.get_cookies()
    cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
    print("🍪 Cookies:", cookie_dict)

    # ✅ Return current page URL and cookies
    return {
        "url": driver.current_url,
        "cookies": cookie_dict
    }
