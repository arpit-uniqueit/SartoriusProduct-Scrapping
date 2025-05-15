
from bs4 import BeautifulSoup
import time
import json
import requests
from lxml import html
import os
from openpyxl import Workbook, load_workbook


def write_to_excel(data):
    headers = ["Item No.", "Product Name", "Product Description", "Product Images",
               "Pack Sizes", "Overview", "Document Links", "Specifications"]
    filename="products.xlsx"

    if not os.path.exists(filename):
        wb = Workbook()
        ws = wb.active
        ws.append(headers)
    else:
        wb = load_workbook(filename)
        ws = wb.active

    ws.append(data)
    wb.save(filename)
    print(f"✅ Data written to {filename}")

def clean_html_description(html_description):
    soup = BeautifulSoup(html_description, "html.parser")

    for sup_tag in soup.find_all("sup"):
        sup_tag.unwrap()

    for b_tag in soup.find_all("b"):
        b_tag.unwrap()

    for ul_tag in soup.find_all("ul"):
        ul_tag.unwrap()
    for li_tag in soup.find_all("li"):
        li_tag.unwrap()

    cleaned_text = soup.get_text("\n", strip=True)

    return cleaned_text

def productDetails(p_url):
    try:
        time.sleep(2)  

        response = requests.get(p_url)

        # Parse the HTML content with lxml

        tree = html.fromstring(response.content)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find('script',type='application/ld+json')
        json_data =json.loads(data.string)

        item_no= json_data['sku']
        print("item no ",item_no)
        print("------------------------------------------------------------------------------------")

        product_name = json_data['name']   
        print("product name ",product_name)
        print("------------------------------------------------------------------------------------")

        product_description = clean_html_description(json_data['description'])
        print("product description ",product_description)
        print("------------------------------------------------------------------------------------")

        product_images = json_data['image']
        print("product images ",product_images)
        print("------------------------------------------------------------------------------------")

        # product_overview = driver.find_element(By.XPATH, "//div[@class='bab-tab-pim-content']")
        product_overview = tree.xpath("//div[@class='bab-tab-pim-content']//p | //div[@class='bab-tab-pim-content']//ul")
        product_overview_text = ""

        for el in product_overview:
            if el.tag == 'p':
                # Process <p> tag, get text and add a newline after each <p>
                text = el.text_content().strip() + "\n"
                product_overview_text += text
            elif el.tag == 'ul':
                # Process <ul> tag by handling each <li> item in the <ul>
                product_overview_text += "\n"
                for li in el.xpath(".//li"):
                    li_text = li.text_content().strip()
                    product_overview_text += f"- {li_text}\n"  # Add bullet point style

        print("Product Overview:", product_overview_text)

        print("------------------------------------------------------------------------------------")

        base_url = "https://shop.sartorius.com/medias"
        pdf_links = tree.xpath('//div[@class="product-download__title"]//a[contains(@href, ".pdf")]/@href')
        full_pdf_urls = [base_url + link +" ," if link.startswith('/') else link+" ," for link in pdf_links]
        print(f"✅ Found {len(full_pdf_urls)} PDF link(s).")
        print("------------------------------------------------------------------------------------")
        full_pdf_urls_text = "\n".join(full_pdf_urls)
        print(full_pdf_urls_text)
        print("------------------------------------------------------------------------------------")

        specification_groups = tree.xpath('//div[@class="specifications"]//div[@class="specifications__group"]')
        specification_lines = []

        for group in specification_groups:
            lines = group.xpath(".//text()")
            for line in lines:
                clean_line = line.strip()
                if clean_line:
                    specification_lines.append(clean_line)

        specification_text = "\n".join(specification_lines)
        print(specification_text)

        write_to_excel([
            item_no,
            product_name,
            product_description,
            product_images,
            "N/A",
            product_overview_text,
            full_pdf_urls_text,
            specification_text
        ])


    except Exception as e:
        print(f"An error occurred: {e}")

productDetails("https://shop.sartorius.com/us/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors")
