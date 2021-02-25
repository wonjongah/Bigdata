from selenium import webdriver
import time

# 자동화된 크롬 창 실행
driver = webdriver.Chrome("../chromedriver")

# 네이버 로그인 페이지 접속
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)

# 시간적 여유 원하는 만큼
time.sleep(2)

# 본인의 아이디, 비밀번호 각각 변수에 저장
my_id = "your_id"
my_pw = "your_password"

# 아이디와 비밀번호 입력
# 파이썬에게 직접 값을 넘겨주는 것이 아니라 자바스크립트로 값을 넘겨줘, 우회해 네이버에 로그인하다.
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_id('log.login').click()
time.sleep(1)

# 코뮤니티 접속
comu_url = "https://cafe.naver.com/codeuniv"
driver.get(comu_url)
time.sleep(1)

# 신규회원게시판 클릭
driver.find_element_by_id("menuLink90").click()
time.sleep(1)

# 프레임 전환 (프레임 name 변수)
driver.switch_to.frame("cafe_main")
time.sleep(1)

# 첫 글 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

# 1부터 20개의 글 크롤링
for i in range(1, 21):
    content = driver.find_element_by_css_selector("div.se-component-content").text
    print(f"< {i}번째 글 >\n{content}\n")
    if i < 20:
        # 마지막 글이면 다음 버튼 누르지 않음
        driver.find_element_by_css_selector("a.BaseButton.btn_next.BaseButton--skinGray.size_default").click()
        time.sleep(1)

driver.close()