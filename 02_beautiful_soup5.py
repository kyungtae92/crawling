import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

# print(bs_obj)
# 이후에
# top_right = bs_obj.find("div", {"class":"area_links"})
# first_a = top_right.find("a")
# print(first_a.text)

# 네이버의 메뉴 이름 뽑아내기
ul = bs_obj.find("ul", {"class":"an_l"})
lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)
