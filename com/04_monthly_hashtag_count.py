import xlsxwriter
import time
# 해시태그를 분석하기 위한 Twitter 모듈
#from konlpy.tag import Twitter
# 크롬 브라우저 조작을 위한 모듈
from selenium import webdriver
# 페이지 스크롤링을 위한 모듈
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import operator

start = time.time()
# 크롤링할 url 주소
url = "https://www.instagram.com/explore/tags/서촌찻집/"
# 다운로드 받은 driver 주소
DRIVER_DIR = '../webdriver/chromedriver.exe'
# 크롬 드라이버를 이용해 임의로 크롬 브라우저를 실행시켜 조작한다.
driver = webdriver.Chrome(DRIVER_DIR)
# 암묵적으로 웹 자원을 (최대) 5초 기다리기
driver.implicitly_wait(5)
# 크롬 브라우저가 실행되며 해당 url로 이동한다.
driver.get(url)
# 총 게시물 수를 클래스 이름으로 찾기
#totalCount = driver.find_element_by_class_name('_fd86t').text
#print("총 게시물:", totalCount)
# body 태그를 태그 이름으로 찾기
elem = driver.find_element_by_tag_name("body")
# alt 속성의 값을 담을 빈 리스트 선언
#alt_list = []
#print(elem)

a_list = []
# 페이지 스크롤을 위해 임시 변수 선언
pagedowns = 1
# 스크롤을 20번 진행한다.
total_post = 179

current_post = 0
last_post = 0
end = 0
#while pagedowns < 100:
while end < 10:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다.
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)
        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)
        a = driver.find_elements_by_css_selector('div.v1Nh3 > a')
        for i in a:
            a_list.append(i.get_attribute('href'))
        pagedowns += 1
        a_list = list(set(a_list))
        current_post = len(a_list)
        if last_post >= current_post:
            end += 1
        else:
            last_post = current_post
            end = 0

date_list = []
date_list2 = []
post = 0
for i in a_list:
    driver.get(i)
    post += 1
    print("post:"+str(post))
    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")
    div = soup.findAll("div", {"class": "C4VMK"})
    if div != None:
        tag_texts = []
        for j in div:
            tags = j.findAll("a")
            for k in tags:
                tag_texts.append(k.text)
        if '#서촌찻집' in tag_texts:
            date = soup.find("time", {"class": "_1o9PC Nzb55"})
            date_list.append(date['datetime'][0:10])
            date_list2.append(date['title'])
w, h = 12,10
monthly = [[0 for x in range(w)] for y in range(h)]
for x in date_list:
    monthly[int(x[0:4])-2010][int(x[5:7])-1] += 1
print(monthly)

#Create Excel File using Xlsxwriter
workbook = xlsxwriter.Workbook('서촌찻집월별.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for i in range(0,10):
    for j in range(0,12):
        worksheet.write(row, col, str(i+2010)+"년"+str(j+1)+"월")
        worksheet.write(row, col+1, monthly[i][j])
        row += 1

workbook.close()


#for x in date_list:
#    worksheet.write(row, col, x)
#    row += 1
#row = 0
#col = 1
#for x in date_list2:
#    worksheet.write(row, col, x)
#    row += 1
#workbook.close()

end = time.time()
elapsed = end - start
print(elapsed)

