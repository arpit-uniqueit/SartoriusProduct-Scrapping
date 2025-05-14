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
import pricedetails


final_notes_main =""
formatted_notes_main=""
key_facts_main=""

def extract_product_data():
    result = [
        {"key facts": key_facts_main},
        {"Formatted Product Summary": formatted_notes_main},
        {"Product Notes": final_notes_main}
    ]

    return result

def support_tag_call(product_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the URL passed as parameter
    driver.get(product_url)

    # Wait for the page to load
    time.sleep(3)
    try:
        accept_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        if accept_btn.is_displayed():
            accept_btn.click()
            # print("Accepted cookies.")
            time.sleep(1)  # Short wait after clicking
    except NoSuchElementException:
        print("Accept Cookies button not found.")
    except ElementClickInterceptedException:
        print("Unable to click the Accept Cookies button.")

    try:
        # Wait until button with exact text "Accept All Cookies" is present and clickable
        wait = WebDriverWait(driver, 5)
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Accept All Cookies']"))
        )
        cookie_button.click()
        print("✅ 'Accept All Cookies' button clicked.")
    except Exception:
        print("ℹ️ 'Accept All Cookies' button not found or already accepted.")
    # # driver.quit()






# Function to open the page and click the Datasheet button
def open_datasheet_page(product_url):
    global final_notes_main, formatted_notes_main, key_facts_main
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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


    # Find the "Datasheet" button using its 'aria-controls' attribute and click it
    try:
        datasheet_tab = driver.find_element(By.CSS_SELECTOR, '[data-cy="datasheet-tab"]')
        datasheet_tab.click()
        print("Clicked datasheet tab.")
    except NoSuchElementException:
        print("Datasheet tab not found.")
        # driver.quit()
        return
    # Wait for the datasheet content to load
    time.sleep(5)

    # Optionally, print the current URL to confirm you're on the right page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Step 5: Extract product titles (you may need to inspect the site for exact class)
    data = soup.find('script',type='application/json')
    json_data =json.loads(data.string)

    def clean_html_notes(html_content):
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract text from <p> tags
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        # Extract list items from <ul>/<li> tags
        list_items = []
        for ul in soup.find_all("ul"):
            for li in ul.find_all("li"):
                list_items.append(f"- {li.get_text(strip=True)}")

        # Combine all content
        full_text = "\n".join(paragraphs + list_items)
        return full_text


    product_notes = json_data['props']['pageProps']['product']['notes']

    # Optional: Mapping note types to readable headers
    note_type_mapping = {
        "targetSummaryMechanical": "Activity summary",
        "targetSummaryBiological": "Biological function summary",
        "pathway": "Pathways",
        "disease": "Associated diseases and disorders"
    }

    combined_output = []

    for note in product_notes:
        note_type = note.get('noteType', 'Note')
        statement_html = note.get('statement', '')
        header = note_type_mapping.get(note_type, note_type.capitalize())

        cleaned_text = clean_html_notes(statement_html)
        combined_output.append(f"{header}\n{cleaned_text}\n")

    # Join all sections into one string
    final_notes = "\n".join(combined_output)
    final_notes_main = final_notes.strip()
    # print("Product Notes:\n", final_notes)

    product_summary = json_data['props']['pageProps']['product']['targetSummaryNotes']
    

    def extract_key_facts(html):
        key_soup = BeautifulSoup(html, "html.parser")

        # Find the Key facts container using its heading
        key_facts_section = key_soup.find("h2", string="Key facts")
        if not key_facts_section:
            return {}

        # Go up to the outer container
        container = key_facts_section.find_parent("div")

        # Now find all <dt> and <dd> pairs inside this container
        key_facts = {}
        for item in container.find_all(["dt", "dd"]):
            if item.name == "dt":
                current_key = item.get_text(strip=True)
            elif item.name == "dd":
                # Extract text including <br> handling
                value = item.get_text(separator="\n", strip=True)
                key_facts[current_key] = value

        return key_facts
    # Extract "Key facts"
    key_facts = extract_key_facts(driver.page_source)
    key_facts_main = key_facts
    # print("Key Facts:", key_facts)



# props.pageProps.product.target.name
    note_type_to_heading = {
                            "targetSummaryMechanical": "Activity summary",
                            "targetSummaryBiological": "Biological function summary",
                            "pathway": "Pathways",
                            "disease": "Associated diseases and disorders"
                            }

    def extract_text_from_html(html_str):
        return BeautifulSoup(html_str, "html.parser").get_text(separator=' ', strip=True)

    formatted_notes = ""
    for note in product_summary:
        heading = note_type_to_heading.get(note["noteType"], note["noteType"])
        body = extract_text_from_html(note["statement"])
        formatted_notes += f"\n{heading}\n{body}\n"

    formatted_notes_main = formatted_notes.strip()

    print("Product Notes:\n", formatted_notes.strip())

    support_tag_call(product_url)
    # driver.quit()

    # Close the browser when done props.pageProps.product.notes
    # driver.quit()

    all_data = extract_product_data()
    return all_data

# Example usage of the function with a product URL
# product_url = "https://www.abcam.com/en-us/products/reagents/phalloidin-ifluor-488-reagent-ab176753"
# open_datasheet_page(product_url)








# data = extract_product_data()
# print(data)