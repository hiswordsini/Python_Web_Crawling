#네이버 페이지의 목록의 제목을 가져오는 프로그램
#메일부터 만화/웹툰까지 불러온다.
#두번에 걸쳐서 불러온다
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span",{"class":"an_txt"})
    print(span.text)

ul = bs_obj.find("ul", {"id":"PM_ID_serviceNavi"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span",{"class":"an_txt"})
    print(span.text)
