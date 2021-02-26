from selenium import webdriver
import time

# 검색 키워드 입력
keyword = input("뉴스 검색 키워드 : ")

# 뉴스 기사 게시판 접속
driver = webdriver.Chrome("../chromedriver")
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)
count = 0

for i in range(3):
    if i != 0:
        num = driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[{i}]')
        num.click()
    # 모든 em.tit 태그를 ten_articles 변수에 저장
    ten_articles = driver.find_elements_by_css_selector('em.tit')

    for article in ten_articles:
        # article은 뉴스 기사 제목의 html이므로 text 붙여서 제목만
        title = article.text
        # 제목 클릭, article은 html이므로 클릭 가능
        article.click()
        time.sleep(1)

        # driver를 새로운 탭 (본문)으로 전환
        driver.switch_to.window(driver.window_handles[-1])
        # 기사 본문을 content 변수에 저장
        content = driver.find_element_by_id('articletxt').text
        seperate = content.split("\n")
        # 기사 본문 출력
        count += 1
        print(f"< {count}번 뉴스 - {title} >")
        
        for sep in seperate:
            # 공백이 아닌 값이라면
            if sep != "":
                print(sep, end = "")
        print("\n")
        # 본문 출력 끝 -> 새로운 탭에서 작업 끝 -> 탭 닫아줌
        driver.close()
        #다시 driver를 맨 처음 탭으로 전환
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

# 크롬 창 닫기
driver.close()