# import requests
# from urllib.parse import urlparse
#
# keyword = "광운대학교"
# url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
# result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
# print(result.json())



# 제이슨
# 딕셔너리 구조

# json = {
#     "name":"kyungtae",
#     "age":"32",
#     "where":"서울",
#     "phone_number":"010-0000-0000",
#     "friends":[{"name":"sian","age":"32"},
#                {"name":"kyuri","age":"34"}]
#     }


# print(json.keys())  # 키값

# print(json['name'])  # value값
# print(json['age'])
# print(json['where'])
# print(json['phone_number'])

# print(json['friends'])  # 리스트값

# friends = json['friends']
# for friend in friends:
#     print(friend)


# friends = json['friends']
# for friend in friends:
#     print(friend["name"])



######################################
# import requests
# from urllib.parse import urlparse
#
# keyword = "광운대학교"
# url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
# result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#
# json_obj = result.json()
# for item in json_obj['items']:
#     print(item)


#####################################
# import requests
# from urllib.parse import urlparse
#
# keyword = "광운대학교"
# url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
# result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#
# json_obj = result.json()
# for item in json_obj['items']:
#     # print("Title : " + item['title'])
#     print("Title : " + item['title'].replace("<b>"," ").replace("</b>"," "),"Link : " + item["link"])  # b태그 없앰 , 링크 받아오기

#######################################
# import requests
# from urllib.parse import urlparse
#
# keyword = "광운대학교"
# url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"
# result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#
# json_obj = result.json()
# print(json_obj)


#####################################
# 함수이용
#
# import requests
# from urllib.parse import urlparse
#
# def get_api_result(keyword, display):
#     url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + str(display)
#     result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#     return result.json()
#
# json_obj = get_api_result("광운대학교", 100)
# print(json_obj)

######################################
# import requests
# from urllib.parse import urlparse
#
# def get_api_result(keyword, display, start):
#     url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
#           + "&display=" + str(display) \
#           + "&start=" + str(start)
#     result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#     return result.json()
#
# json_obj = get_api_result("광운대학교", 100, 1000)
# for item in json_obj['items']:
#     print(item)

#######################################
# import requests
# from urllib.parse import urlparse
#
#
# def get_api_result(keyword, display, start):
#     url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
#           + "&display=" + str(display) \
#           + "&start=" + str(start)
#     result = requests.get(urlparse(url).geturl(),
#                       headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
#                                "X-Naver-Client-Secret":"PAMLZXzubP"})
#     return result.json()
#
#
# def call_and_print(keyword, page):
#     json_obj = get_api_result(keyword, 100, page)
#     for item in json_obj['items']:
#         title = item['title'].replace("<b>", "").replace("</b>", "")
#         print(title + "@" + item['bloggername'] + "@" + item['link'])
#
# keyword = "광운대학교"
# call_and_print(keyword, 1)
# call_and_print(keyword, 101)
# call_and_print(keyword, 201)
# call_and_print(keyword, 301)
# call_and_print(keyword, 401)

#####################################
import requests
from urllib.parse import urlparse


def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
          + "&display=" + str(display) \
          + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"QfPt6cfP9Nse1u1lLZEM",
                               "X-Naver-Client-Secret":"PAMLZXzubP"})
    return result.json()


def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "")
        print(title + "@" + item['bloggername'] + "@" + item['link'])

keyword = "광운대학교"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)