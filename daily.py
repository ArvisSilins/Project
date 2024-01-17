import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://anilist.co/search/anime?format=TV&sort=SCORE_DESC"
driver.get(url)
time.sleep(2)

driver.find_element(By.CLASS_NAME, "css-47sehv").click()
time.sleep(2)

find = driver.find_element(By.XPATH, "//div[@class='media-card']").click()

time.sleep(4)
avarege_score = driver.find_element(By.XPATH,  "//div[@class='el-tooltip data-set']")
score = avarege_score.find_element(By.XPATH, "//div[@class='el-tooltip data-set']//div[@class='value']")
print(score.text)

genres_ = avarege_score.find_element(By.XPATH, "//div[@class='data-set data-list']//div[@class='type'][contains(text(), 'Genres')]")
genres = genres_.find_elements(By.XPATH, "following-sibling::div//a")
for genre in genres:
    print(genre.text)

#next_anime = find.find_element(By.XPATH, "following-sibling::*[1]")
driver.quit()