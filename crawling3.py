#네이버 페이지의 목록의 제목을 가져오는 프로그램
#메일부터 만화/웹툰까지 불러온다.
#한번에 불러온다
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.findAll("ul", {"class":"an_l"})

lis = []
for i in ul:
    lis.append(i.findAll("li"))

for i in lis:
    for li in i:
        a_tag = li.find("a")
        if a_tag == None:
            continue
        span = a_tag.find("span",{"class":"an_txt"})
        print(span.text)
