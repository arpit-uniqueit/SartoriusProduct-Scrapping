# import requests
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-IN,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     # 'referer': 'https://shop.sartorius.com/in/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors',
#     'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
#     'cookie': 'anonymous-consents=%5B%5D; _gcl_au=1.1.765618857.1746938522; _vwo_uuid_v2=D343B49E863A517C36058CD5044D4962A|4c7c977e8280d46722d23a8c9890d686; _ga=GA1.1.1047656229.1746938523; _vwo_uuid=D343B49E863A517C36058CD5044D4962A; _vwo_ds=3%241746938520%3A72.37014521%3A%3A; _mkto_trk=id:481-ZCD-244&token:_mch-sartorius.com-35549708fa2a9ebd6423d05918b5eedf; _fbp=fb.1.1746938523240.682839042690857587; _hjSessionUser_2004235=eyJpZCI6ImE4MjcyYTljLWRlNmYtNTk1NS05ZjMzLWYyNzZiODc4ZDVkYSIsImNyZWF0ZWQiOjE3NDY5Mzg1MjMzNjMsImV4aXN0aW5nIjp0cnVlfQ==; SartSiteWW-cart=59861e5f-6d87-4e23-832a-9fa9e2e53721; ROUTE=.accstorefront-5766f7f58d-lcsft; AKA_A2=A; _vis_opt_s=6%7C; _vis_opt_test_cookie=1; _hjSession_2004235=eyJpZCI6IjVmMDRhOWZhLTNhZTItNDk5MS1iMjgzLTQzMGEzNTNjMjQxYiIsImMiOjE3NDcyODI2OTk0MjMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; JSESSIONID=BFA95EC100D5AD43106534A6DCF2F949.accstorefront-5766f7f58d-lcsft; LastSelectedVariantUrl=/in/p/octet-streptavidin-sa-biosensor/18-5020; _vwo_sn=344166%3A14%3A%3A%3A1; sa-user-id=s%253A0-2d4a16ff-4ae5-4a96-64c7-352b0ed7608e.D2zeoF42GMty4bIZrEnF4E4EzM%252FFyacUwTQSuuGJ4rw; sa-user-id-v2=s%253ALUoW_0rlSpZkxzUrDtdgjg.PmLKqP84NnpMFIadWujuOIklDFNTn6y1O9xFt4sWDQI; sa-user-id-v3=s%253AAQAKIE6VkTlryyUUSgqm5ySuauqDmoVCMw8UwTlVJdJVo7VyEHwYAiDZ7pXBBjoEVEYQwkIEpa4crQ.fbCjPRU%252BsgszE5p7qhA0OL%252FiQlJ2cjvhuBwwg2KpjQc; _ga_Q6F7C10026=GS2.1.s1747282698$o10$g1$t1747285852$j18$l0$h0$db6mTNdj_6i0KUmXxzsTEHNvfoNUPDkS-6A; _uetsid=0d9517402fdf11f0b83077895dd7e07a; _uetvid=4934cd202e2211f09bc9e5a251a75ca1'
# }
#
# response = requests.get(
#     'https://shop.sartorius.com/us/c/biolayer-interferometry',
#     headers=headers,
# )
#
# print(response.text)
# print(response.status_code)
import requests

# Step 1: Send request to the first URL
first_url = "https://shop.sartorius.com/in/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": first_url
}

session = requests.Session()
response1 = session.get(first_url, headers=headers, allow_redirects=True)

# Step 2: Extract cookies from the first response
cookies = session.cookies.get_dict()
print("Cookies from first request:", cookies)

# Step 3: Use the same session to request the second URL (US version)
second_url = "https://shop.sartorius.com/us/p/octet-streptavidin-sa-biosensor/Bio-Layer-Interferometry-SA-Biosensors"
response2 = session.get(second_url, headers={**headers, "Referer": second_url})

# Step 4: Print final results
print("Second request status code:", response2.status_code)
print("Second request final URL:", response2.url)
print("Page title snippet:", response2.text[0:500])  # first 500 chars of HTML

# Optional: Check if redirected (different URL than requested)
if response2.url != second_url:
    print("Redirected to:", response2.url)
