from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=현대&_=1561170013325"

pageString = crawl(url)
bsObj = BeautifulSoup(pageString, "html.parser")
#print(pageString)
print(bsObj)
