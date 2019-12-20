# import requests
# from bs4 import BeautifulSoup
#
# # headers = {"User-Agent": "Mozilla/5.0"}
# url = "http://jolse.com/ "
#
# result = requests.get(url =url)
# # result = requests.get(url, headers=headers)
#
# bs_obj = BeautifulSoup(result.text)
# print(bs_obj)

# 실행하면 403 Forbidden 접근불가라는 메세지



# 접근가능
# import requests
# from bs4 import BeautifulSoup
#
# headers = {"User-Agent": "Mozilla/5.0"}
# url = "http://jolse.com/ "
#
# # result = requests.get(url =url)
# result = requests.get(url, headers=headers)
#
# bs_obj = BeautifulSoup(result.text)
# print(bs_obj)



# 토너 미스트 메뉴에서 화장품이름 추출
# import requests
# from bs4 import BeautifulSoup
#
# headers = {"User-Agent": "Mozilla/5.0"}
# url = "http://jolse.com/category/toners-mists/1019/ "
#
# result = requests.get(url, headers=headers)
#
# bs_obj = BeautifulSoup(result.text)
#
# ul = bs_obj.find("ul", {"class":"prdList grid4"})
# boxs = ul.findAll("div", {"class":"box"})
#
# for box in boxs:
#     ptag = box.find("p", {"class":"name"})
#     span = ptag.find("span")
#     print(span.text)



# 토너 미스트 메뉴에서 화장품가격 추출
# import requests
# from bs4 import BeautifulSoup
#
# headers = {"User-Agent": "Mozilla/5.0"}
# url = "http://jolse.com/category/toners-mists/1019/ "
#
# result = requests.get(url, headers=headers)
#
# bs_obj = BeautifulSoup(result.text)
#
# ul = bs_obj.find("ul", {"class":"prdList grid4"})
# boxs = ul.findAll("div", {"class":"box"})
#
# for box in boxs:
#     ptag = box.find("p", {"class":"name"})
#     span = ptag.find("span")
#     ul = box.find("ul")
#     spans_price = ul.findAll("span")


# 토너 미스트 메뉴에서 화장품가격 추출
# import requests
# from bs4 import BeautifulSoup
#
# headers = {"User-Agent": "Mozilla/5.0"}
# url = "http://jolse.com/category/toners-mists/1019/ "
#
# result = requests.get(url, headers=headers)
#
# bs_obj = BeautifulSoup(result.text)
#
# ul = bs_obj.find("ul", {"class":"prdList grid4"})
# boxs = ul.findAll("div", {"class":"box"})
#
# def get_product_info(box):
#     ptag = box.find("p", {"class":"name"})
#     spans_name = ptag.findAll("span")
#     ul = box.find("ul")
#     spans_price = ul.findAll("span")
#
#     name = spans_name[0].text
#     price = spans_price[1].text
#     print(price)
#
#     return {"name":name, "price":price}
#
# for box in boxs:
#     product_info = get_product_info(box)
#     print(product_info)



# 토너 미스트 메뉴에서 화장품링크 추출
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
url = "http://jolse.com/category/toners-mists/1019/ "

result = requests.get(url, headers=headers)

bs_obj = BeautifulSoup(result.text)

ul = bs_obj.find("ul", {"class":"prdList grid4"})
boxs = ul.findAll("div", {"class":"box"})

def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")

    name = spans_name[0].text
    price = spans_price[1].text
    atag = box.find("a")
    link = atag['href']

    return {"name":name, "price":price, "link":link}

for box in boxs:
    product_info = get_product_info(box)
    print(product_info)