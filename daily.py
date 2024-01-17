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

loop = driver.find_elements(By.XPATH, "//div[@class='results cover']")
#find = driver.find_element(By.XPATH, "//div[@class='media-card']").click()

for ani in loop:
    time.sleep(4)

    find = ani.find_element(By.XPATH, "//div[@class='media-card']")
    find_ = find.find_element(By.XPATH, "following-sibling::div//a").click()
    time.sleep(3)

    avarege_score = driver.find_element(By.XPATH,  "//div[@class='el-tooltip data-set']")
    score = avarege_score.find_element(By.XPATH, "//div[@class='el-tooltip data-set']//div[@class='value']")
    print(score.text)

    genres_ = avarege_score.find_element(By.XPATH, "//div[@class='data-set data-list']//div[@class='type'][contains(text(), 'Genres')]")
    genres = genres_.find_elements(By.XPATH, "following-sibling::div//a")
    for genre in genres:
        print(genre.text)

    driver.back()
    #next_anime = find.find_element(By.XPATH, "following-sibling::*[1]")
driver.quit()