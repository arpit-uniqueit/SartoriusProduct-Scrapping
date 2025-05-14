from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
datasheet_url=""
def support_tag_call(driver, product_url):
    # Open the URL passed as parameter
    driver.get(product_url)

    # Wait for the page to load
    time.sleep(3)
    try:
        accept_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        if accept_btn.is_displayed():
            accept_btn.click()
            print("Accepted cookies.")
            time.sleep(1)  # Short wait after clicking
    except NoSuchElementException:
        print("Accept Cookies button not found.")
    except ElementClickInterceptedException:
        print("Unable to click the Accept Cookies button.")

    try:
        wait = WebDriverWait(driver, 5)
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Accept All Cookies']"))
        )
        cookie_button.click()
        print("✅ 'Accept All Cookies' button clicked.")
    except Exception:
        print("ℹ️ 'Accept All Cookies' button not found or already accepted.")

    # Step 5: Extract product titles (you may need to inspect the site for exact class)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = soup.find('script', type='application/json')
    json_data = json.loads(data.string)
    return json_data

def get_pdf_download_url(driver):
    global datasheet_url
    try:
        wait = WebDriverWait(driver, 10)
        buttons = driver.find_elements(By.XPATH, "//button[@data-cy='download-button']")
        if buttons:
            last_button = wait.until(EC.element_to_be_clickable(buttons[-1]))
            last_button.click()
            print("✅ Clicked last download button")
        else:
            print("❌ No download buttons found")
            return None
    except Exception as e:
        buttons = driver.find_elements(By.XPATH, "//button[@data-cy='download-button']")
        print(f"❌ Error finding/clicking download button: {driver.page_source}")
        return None

    time.sleep(4)  # Wait for download request to trigger

    current_url = driver.current_url
    datasheet_url = current_url
    print(f"✅ The opened page URL after clicking download button is: {current_url}")
     # driver.quit()
    return None


def datasheet_url_data():
    return datasheet_url



def open_datasheet_page(product_url):
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open the product page and perform necessary actions
    product_json = support_tag_call(driver, product_url)
    try:
        support_button = driver.find_element(By.XPATH, "//button[@aria-controls='tabs--panel--3']")
        support_button.click()
        print("✅ 'Support & Downloads' button clicked.")
    except NoSuchElementException:
        print("❌ Support & Downloads button not found.")

    # Get PDF download URL
    pdf_url = get_pdf_download_url(driver)
    if pdf_url:
        print("Download URL:", pdf_url)
    else:
        print("No download URL found.")

    # Close the browser when done
     # driver.quit()

    url_data=datasheet_url_data()
    return url_data

# Example usage of the function with a product URL
# product_url = "https://www.abcam.com/en-us/products/reagents/phalloidin-ifluor-488-reagent-ab176753"
# open_datasheet_page(product_url)


