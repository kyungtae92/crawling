import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url =url)
bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)

# <a>태그에 있는 상세페이지 링크 뽑아내기
# lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# print(lf_items)


# <a>태그에 있는 상세페이지 링크 뽑아내기
# lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# hrefs = [div.find("a")['href'] for div in lf_items]
# print(hrefs)


# Hrefs 변수에 들어있는 링크들의 개수를 세어 링크들을 구분하여 각 서브 페이지에 들어가서 데이터를 뽑아오고자 한다.
# lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# hrefs = [div.find("a")['href'] for div in lf_items]
# print(len(hrefs))


# 특정 범위에 대한 선택적 불러오기
# lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# hrefs = [div.find("a")['href'] for div in lf_items]
# print(len(hrefs[0:5]))
# print(hrefs[0:5])


# 상세페이지 주소 HTML 언어 불러오기
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)


# 상세페이지 내 이름 불러오기
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_name = bs_obj.find("div", {"class":"profile-name"})
#
# profile_h1 = profile_name.find("h1", {"class":"case27-primary-text"})
# print(profile_h1.text)


# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_name = bs_obj.find("div", {"class":"profile-name"})
#
# h1_bp_name = profile_name.find("h1")
# bp_name = h1_bp_name.text
# print(bp_name)


# 상세페이지 내 위치 불러오기
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_loc = bs_obj.find("div", {"class":"buttons medium button-plain"})
# profile_span = profile_loc.find("span", {"class":"button-label"})
# print(profile_span.text)


# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_name = bs_obj.find("div", {"class":"profile-name"})
#
# h1_bp_name = profile_name.find("h1")
# bp_name = h1_bp_name.text
#
# cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
#
# buttons_label = bs_obj.find("span", {"class":"button-label"})
# location = buttons_label.text
# print(location)


# 상세페이지 내 주소값 불러오기
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_url = bs_obj.find("div", {"class":"buttons medium button-outlined"})
# proflie_span = profile_url.find("span", {"class":"button-label"})
# a_tag = proflie_span.find("a")
# print(a_tag['href'])


# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
#
# profile_name = bs_obj.find("div", {"class":"profile-name"})
#
# h1_bp_name = profile_name.find("h1")
# bp_name = h1_bp_name.text
#
# cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
#
# buttons_label = bs_obj.find("span", {"class":"button-label"})
# location = buttons_label.text
#
# lis = cover_buttons.findAll("li")
# li_tag = lis[1]
#
# a_tag = li_tag.find("a")
# link = a_tag['href']
# print(link)


# 함수로 묶어서 이름,위치,링크 한번에 뽑기
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# def get_bp_info(url):
#     result = requests.get(url)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#
#     profile_name = bs_obj.find("div", {"class":"profile-name"})
#     profile_h1 = profile_name.find("h1")
#     print(profile_h1.text)
#
#     profile_loc = bs_obj.find("div", {"class":"buttons medium button-plain"})
#     profile_span = profile_loc.find("span", {"class":"button-label"})
#     print(profile_span.text)
#
#     profile_url = bs_obj.find("div", {"class":"buttons medium button-outlined"})
#     proflie_span = profile_url.find("span", {"class":"button-label"})
#     a_tag = proflie_span.find("a")
#     print(a_tag['href'])


# 딕셔너리에 넣어서 리턴
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# def get_bp_info(url):
#     result = requests.get(url)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#
#     profile_name = bs_obj.find("div", {"class":"profile-name"})
#     profile_h1 = profile_name.find("h1")
#     profile_name = profile_h1.text
#
#     profile_loc = bs_obj.find("div", {"class":"buttons medium button-plain"})
#     profile_span = profile_loc.find("span", {"class":"button-label"})
#     profile_loc = profile_span.text
#
#     profile_url = bs_obj.find("div", {"class":"buttons medium button-outlined"})
#     proflie_span = profile_url.find("span", {"class":"button-label"})
#     a_tag = proflie_span.find("a")
#     profile_url = a_tag.text
#
#     dictionary = {}
#     dictionary['name'] = profile_name
#     dictionary['location'] = profile_loc
#     dictionary['link'] = profile_url
#
#     return dictionary
#
# dic_result = get_bp_info(url)
# print(dic_result)


# 딕셔너리 다 추출
# url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"
#
# def get_bp_info(url):
#     result = requests.get(url)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#
#     profile_name = bs_obj.find("div", {"class":"profile-name"})
#     profile_h1 = profile_name.find("h1")
#     profile_name = profile_h1.text
#
#     profile_loc = bs_obj.find("div", {"class":"buttons medium button-plain"})
#     profile_span = profile_loc.find("span", {"class":"button-label"})
#     profile_loc = profile_span.text
#
#     profile_url = bs_obj.find("div", {"class":"buttons medium button-outlined"})
#     proflie_span = profile_url.find("span", {"class":"button-label"})
#     a_tag = proflie_span.find("a")
#     profile_url = a_tag['href']
#
#     dictionary = {}
#     dictionary['name'] = profile_name
#     dictionary['location'] = profile_loc
#     dictionary['link'] = profile_url
#     return dictionary
#
# lf_items = bs_obj.findAll("div", {"class":"lf-item"})
#
# hrefs = [div.find("a")['href'] for div in lf_items]
#
# for number in range(0, 5):
#     dic_result = get_bp_info(hrefs[number])
#     print(dic_result)