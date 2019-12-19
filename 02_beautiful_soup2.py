import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
print(ul)
print()

li = ul.find("li")
print(li)
print(li.text)
print()

#리스트로 데이터 접근하기
# lis = ul.find("li")
lis = ul.findAll("li")
print(lis)
print()

#인덱스로 데이터 접근하기
lis = ul.findAll("li")
print(lis[0])
print(lis[0].text)
print(lis[1])
print(lis[1].text)
print(lis[2])
print(lis[2].text)
print()
