import requests
import json

from bs4 import BeautifulSoup
import time
import json
import requests
from lxml import html
import re
from urllib.parse import urljoin
import json


cookies = {
    'JSESSIONID': 'B3F1AB2F79C07D8B73EA510794956023.accstorefront-5766f7f58d-2z5gd',
    'ROUTE': '.accstorefront-5766f7f58d-2z5gd',
    'AKA_A2': 'A',
    'anonymous-consents': '%5B%5D',
    '_gcl_au': '1.1.1052955487.1747303155',
    '_vwo_uuid_v2': 'D9ADDBBF335F9004054B5471E653CD4D7|913634ba5da96de201b92c2ad82045f5',
    '_vwo_uuid': 'D9ADDBBF335F9004054B5471E653CD4D7',
    '_vwo_ds': '3%241747303156%3A89.40560402%3A%3A',
    '_ga': 'GA1.1.1763175026.1747303157',
    '_mkto_trk': 'id:481-ZCD-244&token:_mch-sartorius.com-402dd1c336e9d8d4cd35bab66559239a',
    '_hjSession_2004235': 'eyJpZCI6IjYyZDUyNWYyLWZiMjItNGU3Yy05NzJhLWUxODU0NGQ5MTBlNyIsImMiOjE3NDczMDMxNTc2NDQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
    '_fbp': 'fb.1.1747303157737.963266987621388730',
    '_vis_opt_s': '1%7C',
    '_vis_opt_test_cookie': '1',
    '_hjSessionUser_2004235': 'eyJpZCI6IjIwY2EwZmEyLTAwNDEtNWM1NS1hYTJlLWI4NTUwMTA3ZTQ5YSIsImNyZWF0ZWQiOjE3NDczMDMxNTc2MzgsImV4aXN0aW5nIjp0cnVlfQ==',
    'sa-user-id': 's%253A0-079cb576-466e-5b44-4a4c-2e5a5e877ab4.5hiFlDGBRwVjnDczTnq8%252FGMB1pCK2OxPiilrRyNOsIE',
    'sa-user-id-v2': 's%253AB5y1dkZuW0RKTC5aXod6tGgc0Z4.Ekb3Ji7e%252Fgmp0NyJLvQ5G%252Fh8Ts%252BpXqtD%252Fkbjg2W2wtk',
    '_vwo_sn': '0%3A8%3A%3A%3A1',
    'LastSelectedVariantUrl': '/us/p/octet-anti-penta-his-his1k-biosensors/Bio-Layer-Interferometry-HIS1K-Biosensors',
    'sa-user-id-v3': 's%253AAQAKIJx_HTDig5S98hXJdNtIqAT8mKhvQF8SzMyikrduFC-OEHwYBCDn-5bBBjABOgRURhDCQgQqfsQ3.gUgHZjy6TCCbWI56%252BkJgZl4zd9QRoxNMxspORMJtm4Q',
    '_uetsid': '43f32f10317311f08a0193398d14ef64',
    '_uetvid': '43f395c0317311f08f3fe7bde0604c3f',
    '_ga_Q6F7C10026': 'GS2.1.s1747303157$o1$g1$t1747303948$j60$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': 'JSESSIONID=B3F1AB2F79C07D8B73EA510794956023.accstorefront-5766f7f58d-2z5gd; ROUTE=.accstorefront-5766f7f58d-2z5gd; AKA_A2=A; anonymous-consents=%5B%5D; _gcl_au=1.1.1052955487.1747303155; _vwo_uuid_v2=D9ADDBBF335F9004054B5471E653CD4D7|913634ba5da96de201b92c2ad82045f5; _vwo_uuid=D9ADDBBF335F9004054B5471E653CD4D7; _vwo_ds=3%241747303156%3A89.40560402%3A%3A; _ga=GA1.1.1763175026.1747303157; _mkto_trk=id:481-ZCD-244&token:_mch-sartorius.com-402dd1c336e9d8d4cd35bab66559239a; _hjSession_2004235=eyJpZCI6IjYyZDUyNWYyLWZiMjItNGU3Yy05NzJhLWUxODU0NGQ5MTBlNyIsImMiOjE3NDczMDMxNTc2NDQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _fbp=fb.1.1747303157737.963266987621388730; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _hjSessionUser_2004235=eyJpZCI6IjIwY2EwZmEyLTAwNDEtNWM1NS1hYTJlLWI4NTUwMTA3ZTQ5YSIsImNyZWF0ZWQiOjE3NDczMDMxNTc2MzgsImV4aXN0aW5nIjp0cnVlfQ==; sa-user-id=s%253A0-079cb576-466e-5b44-4a4c-2e5a5e877ab4.5hiFlDGBRwVjnDczTnq8%252FGMB1pCK2OxPiilrRyNOsIE; sa-user-id-v2=s%253AB5y1dkZuW0RKTC5aXod6tGgc0Z4.Ekb3Ji7e%252Fgmp0NyJLvQ5G%252Fh8Ts%252BpXqtD%252Fkbjg2W2wtk; _vwo_sn=0%3A8%3A%3A%3A1; LastSelectedVariantUrl=/us/p/octet-anti-penta-his-his1k-biosensors/Bio-Layer-Interferometry-HIS1K-Biosensors; sa-user-id-v3=s%253AAQAKIJx_HTDig5S98hXJdNtIqAT8mKhvQF8SzMyikrduFC-OEHwYBCDn-5bBBjABOgRURhDCQgQqfsQ3.gUgHZjy6TCCbWI56%252BkJgZl4zd9QRoxNMxspORMJtm4Q; _uetsid=43f32f10317311f08a0193398d14ef64; _uetvid=43f395c0317311f08f3fe7bde0604c3f; _ga_Q6F7C10026=GS2.1.s1747303157$o1$g1$t1747303948$j60$l0$h0',
}



params = {
    'country': 'US',
    'quantity': '1',
}
def get_product_price(p_url, cookies_dy):
    
    response = requests.get(p_url,headers=headers, cookies=cookies_dy)
    time.sleep(12)

    tree = html.fromstring(response.content)
    soup = BeautifulSoup(response.text, 'html.parser')

    pack_size = tree.xpath("//div[contains(@class, 'page-details-variants-select-component')]"
                         "//div[@class='variant-section']//ul[@class='variantSelectionList']"
                         "//li//button[@aria-pressed='true']//text()")
    pack_size_text = "".join(pack_size).strip()

    data = soup.find('script',type='application/ld+json')
    # json_data =json.loads(data.string)

    pack_sixe_price = tree.xpath("//div[@class='pdf-product-price-amount']/text()")
    pack_sixe_price = "US$ " + "".join(pack_sixe_price).strip()


    one_data=({
             "Pack Size": pack_size_text,
             "Product Price": pack_sixe_price
         })
         
    buttons = tree.xpath("//div[contains(@class, 'page-details-variants-select-component')]"
                         "//div[@class='variant-section']"
                         "//ul[@class='variantSelectionList']//li//button[@aria-pressed='false']")
    results = []
    results.append(one_data)
    for btn in buttons:
        try:
            # Get pack size
            pack_size = btn.text_content().strip()

            # Extract relative href from onclick attribute
            onclick = btn.attrib.get("onclick", "")
            match = re.search(r"location\.href='([^']+)'", onclick)
            if not match:
                continue
            relative_url = match.group(1)

            # Convert to full URL
            full_href = urljoin("https://shop.sartorius.com/", relative_url)

            # Request that variant URL
            variant_response = requests.get(full_href, headers=headers, cookies=cookies)

            # Extract price (modify if needed)
            price_match = re.search(r'"price"\s*:\s*"?(\d+)"?', variant_response.text)
            if not price_match:
                continue
            amount = price_match.group(1)
            amount = 'US$ ' + amount

            # Store result
            results.append({
                "Pack Size": pack_size,
                "Product Price": amount
            })

        except Exception as e:
            print("⚠️ Error:", e)
    return results

        # print("Selected Button Value:", pack_size.text_content().strip())
