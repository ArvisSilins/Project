import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--ignore-certificate-errors")
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://anilist.co/search/anime?format=TV&sort=SCORE_DESC"
driver.get(url)
time.sleep(2)

driver.find_element(By.CLASS_NAME, "css-47sehv").click()
time.sleep(2)

#loop = driver.find_elements(By.XPATH, "//div[@class='results cover']")
find = driver.find_element(By.XPATH, "//div[@class='media-card']")
finds = find.find_elements(By.XPATH, ".//a[@class='cover']")

for ani in finds:
    time.sleep(4)

    ani.click()

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