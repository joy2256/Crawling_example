from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver  = webdriver.Chrome(options=options)

url_str = "https://www.tripadvisor.co.kr/Hotel_Review-g294197-d20886229-Reviews-or"
url_num = str(0)
url_keyword = "-Mondrian_Seoul_Itaewon-Seoul.html"
total_url = url_str + url_num + url_keyword
driver.get(total_url)

#time.sleep(3)

# 더보기 클릭
review = driver.find_element_by_css_selector("#component_14 > div > div:nth-child(3) > div:nth-child(3) > div.oETBfkHU > div._3hDPbqWO > div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span")
time.sleep(3)
print(review.text)
   