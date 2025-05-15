from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# US Proxy
PROXY = "170.39.76.48:3128"  # Replace with a valid proxy if needed

# Chrome options
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server=http://{PROXY}')
chrome_options.add_argument("--headless")  # run without opening window
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--lang=en-US")

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Target URL
url = "https://shop.sartorius.com/us/c/biolayer-interferometry"
driver.get(url)
time.sleep(5)  # wait for page to load

# Print current URL
print("Final URL:", driver.current_url)
print("Title:", driver.title)

# Extract all product links
product_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/us/p/')]")
print(f"Number of product links found: {len(product_links)}")
# Use a set to avoid duplicates
urls = set()
for link in product_links:
    href = link.get_attribute("href")
    if href:
        urls.add(href)
        

# Print each product URL
print("\nProduct URLs found:")
for url in urls:
    print(url)

driver.quit()
