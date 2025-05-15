import requests
import json

from bs4 import BeautifulSoup
import time
import json
import requests
from lxml import html
cookies = {
    '_gcl_au': '1.1.418745738.1746937171',
    '_ga': 'GA1.1.1092704647.1746937171',
    'dd_anonymous_id': '81a439fc-eceb-41ee-abd5-c286b11d3518',
    '_fbp': 'fb.1.1746937171635.777369643318052359',
    'OptanonAlertBoxClosed': '2025-05-11T04:19:32.904Z',
    'ak_bmsc': '0FA4E95045E4390897B45EB31258285E~000000000000000000000000000000~YAAQBmfRFwDGNbSWAQAAopzwxRsY4/Lc5t28eG86bbXZkTi38b5HvfdXF5UQlkLMXhiVX75uqeQlkR0Ot7c+8aO/dpNTYVvs9tRoE/ROpnD18lsaMoqB6cUUjJ9ZhDxEsW0ylmMan7ivzUE1JyUek5U8OLNC94pQYKdCK2vSwV60K7P+Va0XkQSAtE4wl9gFNF7GNTA60ztY6gIV8IGg2xpN4vkiaO5WNARkm4wVn7dShY6WXG9S3Mrk/4Pur/YGCUsxFrsRJjHDBaVfNROM9Ovvh+KVXUZNfyYUUXU/chB48/WtmLIccyWUMgoFpEnfOYFPv/AG85NBSl7XtVArs7+R9yvdU0RuerQFX5JsZphBRkQsX/hk3gliPNr2R8/r/V3CliC8Q+tc2rBQ+CtBUYygAiTSH2Y3tzTtC0XuHdbFGTANzOlgBMIVfqhN7qGTb1iMkW3KDPupQPM=',
    'bm_ss': 'ab8e18ef4e',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+May+13+2025+01%3A53%3A21+GMT%2B0530+(India+Standard+Time)&version=202503.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5882345f-9f01-4672-8837-8392047f17d9&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false',
    '_uetsid': '1c372a402f6611f0bb982f950e6cbe1c',
    '_uetvid': '232567002e1f11f09ba06fe16b072e04',
    'da_sid': 'CC6BE54B8E33AEB7DA56AA13A29388A8FF.1|3|0|3',
    'da_lid': '34B14E159A78EA34A2A4BB99E0E9A3C59F|0|0|0',
    'da_intState': '0',
    'bm_so': '66B47135C1B44C670C4323F70D8061E7B949156277A361DA4168DF5862C6CB9E~YAAQfF3SF98ChIaWAQAApy0rxgPqjHW2KMxmnJxOQYhTIuIOSti0rtLVgWgjyCWhksbKy4bu8Nb5ooDlwGyDMExPtRtKmLWYCCRAHNCQ4PHRN/9ikDimbryQcZHqgvflCa71sCeaPgz7e/epaGb0MRO4rzl2NGKEc0iXQonnv+U5rLNEiM49r1s7sc7BFyopOmPWqXHbQ2oaCViN9A9UJ3oX8vDThcq9ZM8YEIzfo3wNCa42Hdy1NQZvRhrQAVf5Y6hw1KoJpRLgL4e1yx6085EAR/fGHwa7xZLmF8Uoc8AAR/wN6bCr7WtNT6bRYwNISQpZ9GNAdsvb8ss4DjwnQ7RGu5kU8DzP27DUB96Uk4OmBwRiwQ31OpR3VsssDN5Hfx9322Yo14Zhj+WeYqS+xbSdwQfUM7oGVia0KajHfnUhO9iIYOONZWA9lZi9FPx/6otQygPL3AZ04N4=',
    '_ga_LTF3E70SKQ': 'GS2.1.s1747077603$o4$g1$t1747081440$j12$l0$h0',
    'bm_s': 'YAAQeTLUFyAuRsSWAQAAtT0rxgN3RumNZ2/p/qoZ2k0+0mEcUJeeNff+swCqlImOzFSO1UGgEJxDbHa2b9C197GabUFW3o5YjQ5ceiHORdbceZmR00gbagUG2poc3YzjAUmhjgNwOF9lS9TMVms++XKzrLhL3TyDVXDieRSAUhCuOEeE3Kboqhja/cvmFyOzmiFBmsSINEfk5NbzKiRCwut6T0AAURmhbLGO5gdCQfinZQmSFzDy7n4sZ01AUvnrk1U/Lcixw+AqiYz6Eilg3yy1s9SOhQ2MOq6jY//oCM9a9aBRsriE/GLuEiZ3nmi8m0CAFsA6XRR1lmhupTXBMnXn5aVg0wx0YCk19WIfPT39Qp1KTIfITTYBdwqcB+macvj74/e/blpUMU7IE9q9C0DMjTCPGvwMc9dzOVsa6gqGJfKCFOZQApaEIOpMDY3dGglBv4n4V0u6AfI/vBMvFIw5Mb6ffZE+fQoqNS7/Z728XzurDsEDsV2RfYkZLpwmFVPqU9FkaCENK1DF7evIUn77Lob6mdSXQ7CWK+FZtuno+e7pB9iu1/7qe+yDMozfkwo=',
    'bm_sv': 'A30C77B0D77613CD0316935FB6C3D2BE~YAAQeTLUFyEuRsSWAQAAtT0rxhuvM5f4kqMi6od/A2GvY0yU18e2EJ9qRLDcttAyl1olIq/X22uB+LShG6dEYepywxag9If9hkoaSA+tyoylB6NqapiPXsDf6LWwvxFe7+jOk4iTLU8IQ/XNt1DJS6pdeOShnvWvCQIS61AD9eaCsNufkKVKbNOsSdF2wAB8A3xTHJp/A829XrSAhmR5D8hrVSE1/vpjDJYHCqWxtiWFPxGNpf1hcRPtePPABxGg~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,gu;q=0.6',
    'origin': 'https://www.abcam.com',
    'priority': 'u=1, i',
    'referer': 'https://www.abcam.com/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-abcam-app-id': 'b2c-public-website',
    # 'cookie': '_gcl_au=1.1.418745738.1746937171; _ga=GA1.1.1092704647.1746937171; dd_anonymous_id=81a439fc-eceb-41ee-abd5-c286b11d3518; _fbp=fb.1.1746937171635.777369643318052359; OptanonAlertBoxClosed=2025-05-11T04:19:32.904Z; ak_bmsc=0FA4E95045E4390897B45EB31258285E~000000000000000000000000000000~YAAQBmfRFwDGNbSWAQAAopzwxRsY4/Lc5t28eG86bbXZkTi38b5HvfdXF5UQlkLMXhiVX75uqeQlkR0Ot7c+8aO/dpNTYVvs9tRoE/ROpnD18lsaMoqB6cUUjJ9ZhDxEsW0ylmMan7ivzUE1JyUek5U8OLNC94pQYKdCK2vSwV60K7P+Va0XkQSAtE4wl9gFNF7GNTA60ztY6gIV8IGg2xpN4vkiaO5WNARkm4wVn7dShY6WXG9S3Mrk/4Pur/YGCUsxFrsRJjHDBaVfNROM9Ovvh+KVXUZNfyYUUXU/chB48/WtmLIccyWUMgoFpEnfOYFPv/AG85NBSl7XtVArs7+R9yvdU0RuerQFX5JsZphBRkQsX/hk3gliPNr2R8/r/V3CliC8Q+tc2rBQ+CtBUYygAiTSH2Y3tzTtC0XuHdbFGTANzOlgBMIVfqhN7qGTb1iMkW3KDPupQPM=; bm_ss=ab8e18ef4e; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+13+2025+01%3A53%3A21+GMT%2B0530+(India+Standard+Time)&version=202503.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5882345f-9f01-4672-8837-8392047f17d9&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=IN%3BGJ&AwaitingReconsent=false; _uetsid=1c372a402f6611f0bb982f950e6cbe1c; _uetvid=232567002e1f11f09ba06fe16b072e04; da_sid=CC6BE54B8E33AEB7DA56AA13A29388A8FF.1|3|0|3; da_lid=34B14E159A78EA34A2A4BB99E0E9A3C59F|0|0|0; da_intState=0; bm_so=66B47135C1B44C670C4323F70D8061E7B949156277A361DA4168DF5862C6CB9E~YAAQfF3SF98ChIaWAQAApy0rxgPqjHW2KMxmnJxOQYhTIuIOSti0rtLVgWgjyCWhksbKy4bu8Nb5ooDlwGyDMExPtRtKmLWYCCRAHNCQ4PHRN/9ikDimbryQcZHqgvflCa71sCeaPgz7e/epaGb0MRO4rzl2NGKEc0iXQonnv+U5rLNEiM49r1s7sc7BFyopOmPWqXHbQ2oaCViN9A9UJ3oX8vDThcq9ZM8YEIzfo3wNCa42Hdy1NQZvRhrQAVf5Y6hw1KoJpRLgL4e1yx6085EAR/fGHwa7xZLmF8Uoc8AAR/wN6bCr7WtNT6bRYwNISQpZ9GNAdsvb8ss4DjwnQ7RGu5kU8DzP27DUB96Uk4OmBwRiwQ31OpR3VsssDN5Hfx9322Yo14Zhj+WeYqS+xbSdwQfUM7oGVia0KajHfnUhO9iIYOONZWA9lZi9FPx/6otQygPL3AZ04N4=; _ga_LTF3E70SKQ=GS2.1.s1747077603$o4$g1$t1747081440$j12$l0$h0; bm_s=YAAQeTLUFyAuRsSWAQAAtT0rxgN3RumNZ2/p/qoZ2k0+0mEcUJeeNff+swCqlImOzFSO1UGgEJxDbHa2b9C197GabUFW3o5YjQ5ceiHORdbceZmR00gbagUG2poc3YzjAUmhjgNwOF9lS9TMVms++XKzrLhL3TyDVXDieRSAUhCuOEeE3Kboqhja/cvmFyOzmiFBmsSINEfk5NbzKiRCwut6T0AAURmhbLGO5gdCQfinZQmSFzDy7n4sZ01AUvnrk1U/Lcixw+AqiYz6Eilg3yy1s9SOhQ2MOq6jY//oCM9a9aBRsriE/GLuEiZ3nmi8m0CAFsA6XRR1lmhupTXBMnXn5aVg0wx0YCk19WIfPT39Qp1KTIfITTYBdwqcB+macvj74/e/blpUMU7IE9q9C0DMjTCPGvwMc9dzOVsa6gqGJfKCFOZQApaEIOpMDY3dGglBv4n4V0u6AfI/vBMvFIw5Mb6ffZE+fQoqNS7/Z728XzurDsEDsV2RfYkZLpwmFVPqU9FkaCENK1DF7evIUn77Lob6mdSXQ7CWK+FZtuno+e7pB9iu1/7qe+yDMozfkwo=; bm_sv=A30C77B0D77613CD0316935FB6C3D2BE~YAAQeTLUFyEuRsSWAQAAtT0rxhuvM5f4kqMi6od/A2GvY0yU18e2EJ9qRLDcttAyl1olIq/X22uB+LShG6dEYepywxag9If9hkoaSA+tyoylB6NqapiPXsDf6LWwvxFe7+jOk4iTLU8IQ/XNt1DJS6pdeOShnvWvCQIS61AD9eaCsNufkKVKbNOsSdF2wAB8A3xTHJp/A829XrSAhmR5D8hrVSE1/vpjDJYHCqWxtiWFPxGNpf1hcRPtePPABxGg~1',
}

params = {
    'country': 'US',
    'quantity': '1',
}
def get_product_price(pro_url):
    
    response = requests.get(pro_url)
    time.sleep(22)

    tree = html.fromstring(response.content)
    soup = BeautifulSoup(response.text, 'html.parser')

    pack_size = tree.xpath("//div[contains(@class, 'page-details-variants-select-component')]"
                         "//div[@class='variant-section']//ul[@class='variantSelectionList']"
                         "//li//button[@aria-pressed='true']//text()")
    pack_size_text = "".join(pack_size).strip()
    print(pack_size_text)

    data = soup.find('script',type='application/ld+json')
    json_data =json.loads(data.string)

    pack_sixe_price = tree.xpath("//div[@class='pdf-product-price-amount']/text()")
     
    print("Pack Size Price:", pack_sixe_price)
        # print("Selected Button Value:", pack_size.text_content().strip())

get_product_price("https://shop.sartorius.com/us/p/octet-streptavidin-sa-biosensor/18-5019")