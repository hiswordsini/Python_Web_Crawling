import requests
import bs4

def get_product_info(box):
    ptag = box.find("p", {"class": "name"})
    spans_name = ptag.find("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    #print(len(spans_price))
    name = spans_name.text
    if len(spans_price) >= 4:
        price = spans_price[4].text
    else:
        price = spans_price[1].text

    atag = box.find("a")
    link = "jolse.com"+atag['href']
    #print(price)

    return {"name":name, "price":price, "link":link}

def get_page_products(url,headers):
    # http 403 forbidden error 막기 위해 headers 부분을 추가해야함
    result = requests.get(url, headers=headers)

    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul", {"class": "prdList grid4"})

    boxes = ul.findAll("div", {"class": "box"})

    product_info_list = [get_product_info(box) for box in boxes]

    return product_info_list

urls = [
    "http://jolse.com/category/tonermist/43/?page=1",
    "http://jolse.com/category/tonermist/43/?page=2",
    "http://jolse.com/category/tonermist/43/?page=3",
    "http://jolse.com/category/tonermist/43/?page=4",
    "http://jolse.com/category/tonermist/43/?page=5",
    "http://jolse.com/category/tonermist/43/?page=6",
    "http://jolse.com/category/tonermist/43/?page=7",
    "http://jolse.com/category/tonermist/43/?page=8"
]

#http 403 forbidden error 막기 위해 추가해야함
headers = {'User-Agent': 'Chrome/74.0.3729.169'}
for page_number in range(0,8):
    page_products = get_page_products(urls[page_number],headers)
    print(page_products)

