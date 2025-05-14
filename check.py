from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# Chrome setup
options = Options()
# options.add_argument("--headless=new")  # Use headless only if needed
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

def DocumentLinks(p_url):
    try:

        driver.get(p_url)
        time.sleep(60)
        # Wait for cookie popup and click the accept/agree button
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            print("Cookie accepted.")
        except Exception as e:
            print("Cookie button not found or already accepted:", e)

        # Step 1: Accept Cookies
        '''
        try:
            agree_button = wait.until(EC.element_to_be_clickable((By.ID, "accept")))
            agree_button.click()
            print("Cookies accepted.")
        except:
            print("No cookie banner found or already accepted.")

        # Step 2: Country selection (if shown)
        try:
            country_select = wait.until(EC.presence_of_element_located((By.ID, "country-select")))
            select = Select(country_select)
            select.select_by_visible_text("United States")
            print("Country selected.")

            save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-js-submit='']")))
            save_button.click()
            print("Country selection saved.")
        except:
            print("Country selection not shown or already saved.")

        # Step 3: Wait until cookie modal is gone
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "usercentrics-cmp-ui")))
            print("Cookie modal closed.")
        except:
            print("No cookie modal found.")

            '''
        
        ''''
        # Step 4: Click "Documents" tab
        document_tab = wait.until(EC.element_to_be_clickable((By.ID, "documentsTabHeader")))
        driver.execute_script("arguments[0].scrollIntoView(true);", document_tab)
        time.sleep(1)  # small delay to ensure visibility
        document_tab.click()
        print("Documents tab clicked.")

        # Step 5: Wait for links and scrape
        time.sleep(3)
        pdf_links = driver.find_elements(By.XPATH, '//div[@class="product-download__title"]//a[contains(@href, ".pdf")]')
        for link in pdf_links:
            print(link.get_attribute("href"))

        print("Total PDF links found:", len(pdf_links))
        '''

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Usage:
DocumentLinks("https://shop.sartorius.com/us/p/octet-streptavidin-sa-biosensor/18-5020")
