import requests
from lxml import html
import _init_

url = "https://shop.sartorius.com/in/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
tree = html.fromstring(response.content)

elements = tree.xpath('//div[@class="bab-e-shadow-category__categories"]//div//a')

for el in elements:
    href = el.xpath('./@href')
    category = el.text_content().strip()
    full_url=url+href[0] 
    _init_.get_ll_product_data_from_url(full_url,category)
    print(f"Text: {category}, Href: {full_url if href else 'N/A'}")
