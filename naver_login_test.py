from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver  = webdriver.Chrome(options=options)
driver.get("https://www.naver.com/")
naver_id = 'joy2256'
naver_pw = 'joyjoyjoy12.'

#로그인 위치 찾아서 클릭
login_btn = driver.find_element_by_css_selector('#account > a')
login_btn.click()

# input_id = driver.find_element_by_css_selector('#id')
# input_pw = driver.find_element_by_css_selector('#pw')
# input_id.send_keys(naver_id)
# input_pw.send_keys(naver_pw)

#네이버의 자동로그인 보안 때문에 자바스크립트로 우회
driver.execute_script(f"document.getElementsByName('id')[0].value='{naver_id}'")  # id 입력
driver.execute_script(f"document.getElementsByName('pw')[0].value='{naver_pw}'")  # pw 입력

driver.find_element_by_css_selector("#log\.login").click()