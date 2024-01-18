import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

options = Options()
options.add_argument("--ignore-certificate-errors")
service = Service(ChromeDriverManager().install())
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://anilist.co/search/anime?format=TV&sort=SCORE_DESC"
driver.get(url)
time.sleep(2)

driver.find_element(By.CLASS_NAME, "css-47sehv").click()
time.sleep(2)

while True:
    try:
        #loop = driver.find_elements(By.XPATH, "//div[@class='results cover']")
        find = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='media-card']/a[@class='cover']")))
        
        anime_links = [link.get_attribute("href") for link in find]

        for anime_link in anime_links:
            time.sleep(4)

            driver.get(anime_link)

            time.sleep(3)

            avarege_score = driver.find_element(By.XPATH,  "//div[@class='el-tooltip data-set']")
            score = avarege_score.find_element(By.XPATH, "//div[@class='el-tooltip data-set']//div[@class='value']")
            print(score.text)

            genres_ = avarege_score.find_element(By.XPATH, "//div[@class='data-set data-list']//div[@class='type'][contains(text(), 'Genres')]")
            genres = genres_.find_elements(By.XPATH, "following-sibling::div//a")
            for genre in genres:
                print(genre.text)

            driver.back()
            time.sleep(2) 
    except NoSuchElementException:
        print("No more anime to scrape.")
        break
    #next_anime = find.find_element(By.XPATH, "following-sibling::*[1]")
driver.quit()