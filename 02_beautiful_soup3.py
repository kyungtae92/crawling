#태그별 접근 방법
import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

# ul = bs_obj.find("ul")
# ul = bs_obj.findAll("ul")
# print(ul)

# 클래스를 설정할시
ul = bs_obj.find("ul", {"class":"reply"})
print(ul)
print(ul.text)