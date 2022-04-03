from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

broswer = webdriver.Chrome()
url = "https://www.naver.com"
broswer.get(url)
broswer.implicitly_wait(10)
broswer.maximize_window()

# 쇼핑 메뉴 클릭
broswer.find_element_by_css_selector('.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = broswer.find_element_by_css_selector('.co_srh_input._input')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = broswer.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    broswer.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = broswer.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성 (경로, 쓰기모드, 인코딩, 줄바꿈 없애기)
file = open(r"C:\hcoding\selenium\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(file)

# 상품 정보 div
items = broswer.find_elements_by_css_selector('.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.basicList_price_area__1UXXR').text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name,price,link)
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])

# 파일 닫기
file.close()

# commit

