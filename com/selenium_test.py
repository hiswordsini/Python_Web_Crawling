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
while end < 5:
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

tags_data = {}
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
            for k in tag_texts:
                if k[0] != '#':
                    continue
                else:
                    if not (k in tags_data):
                        tags_data[k] = 0
                    tags_data[k] += 1
#hashno = sorted(tags_data, key=lambda k : tags_data[k], reverse=True)
hash = sorted(tags_data.items(), key=operator.itemgetter(1), reverse=True)
print(len(tags_data))
print(hash)
#Create Excel File using Xlsxwriter
workbook = xlsxwriter.Workbook('서촌찻집3.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for x in hash:
    worksheet.write(row, col, x[0])
    worksheet.write(row, col+1, x[1])
    row += 1
    col = 0
workbook.close()

end = time.time()
elapsed = end - start
print(elapsed)

# 값의 중복을 방지를 리스트 set으로 변환후 리스트로 재할당
#alt_list = list(set(alt_list))
# 키:해시태그, 값:횟수 형식으로 저장하기 위한 빈 딕셔너리 선언
#dict_data = {}
# alt 속성의 값인 제목과 해시태그 중 해시태그 만을 가져오기 위한 Tiwitter 객체 생성
#tw = Twitter()
# alt_list에 담긴 값의 크기만큼 반복한다.
#for alt in alt_list:
    # pos 메서드를 통해 alt 속성의 모든 해시태그의 값을 (값, 품사) 형태의 튜플을 요소로 갖는 리스트로 반환한다.
#    temp = tw.pos(alt, norm = True)
    # 리스트의 크기만큼 반복한다.
 #   for data in temp:
        # 품사가 만약 해시태그이면
 #       if data[1] == "Hashtag":
            # 결과 값을 저장할 딕셔너리에 값이 있는지 확인하고 없다면 새로이 키를 추가하고 0, 있다면 기존 키에 1을 더해준다.
 #           if not (data[0] in dict_data):
 #               dict_data[data[0]] = 0
 #           dict_data[data[0]] += 1

# 딕셔너리를 횟수를 가지고 내림차순으로 정렬한다.
#keys = sorted(dict_data.items(), key = lambda x:x[1], reverse = True)
# 1~15위 까지의 키:값을 출력한다.
#for k, v in keys[:15]:
#    print("{}({})".format(k, v))

# 드라이버를 종료한다.
#driver.close()