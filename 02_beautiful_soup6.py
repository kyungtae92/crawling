import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

# 네이버 뉴스기사 가져오기
news = bs_obj.findAll("ul", {"class":"mlist2 no_bg"})
lis = news[1].findAll("li")

for li in lis:
    strong = li.find("strong")
    print(strong.text)