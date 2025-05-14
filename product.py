
from bs4 import BeautifulSoup
import time
import json
import requests
from lxml import html


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

        product_description = clean_html_description(json_data['description'])
        print("product description ",product_description)
        print("------------------------------------------------------------------------------------")

        product_images = json_data['image']
        print("product images ",product_images)
        print("------------------------------------------------------------------------------------")

        # product_overview = driver.find_element(By.XPATH, "//div[@class='bab-tab-pim-content']")
        product_overview = tree.xpath("//div[@class='bab-tab-pim-content']")
        product_overview_text = "\n".join([el.text_content().strip() for el in product_overview])
        print("Product Overview:", product_overview_text)
        print("------------------------------------------------------------------------------------")

        base_url = "https://shop.sartorius.com/medias"
        pdf_links = tree.xpath('//div[@class="product-download__title"]//a[contains(@href, ".pdf")]/@href')
        full_pdf_urls = [base_url + link if link.startswith('/') else link for link in pdf_links]
        print(f"✅ Found {len(full_pdf_urls)} PDF link(s).")
        print("------------------------------------------------------------------------------------")
        print(full_pdf_urls[0])
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


    except Exception as e:
        print(f"An error occurred: {e}")

productDetails("https://shop.sartorius.com/us/p/octet-streptavidin-sa-biosensor/18-5020")
