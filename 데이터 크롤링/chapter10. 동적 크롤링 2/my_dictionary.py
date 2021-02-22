from selenium import webdriver
import time

my_dict = {}

def get_papago_result(driver, dict):
    question = input('번역할 영단어 입력 : ')
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click()

    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    dict[question] = output
    driver.find_element_by_css_selector("textarea#txtSource").clear()

    return output

driver = webdriver.Chrome('../chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

for i in range(3):
    print(get_papago_result(driver, my_dict))

print(my_dict)

driver.close()