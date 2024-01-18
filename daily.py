import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--ignore-certificate-errors")
service = Service(ChromeDriverManager().install())
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://anilist.co/search/anime?format=TV&sort=SCORE_DESC"
driver.get(url)
time.sleep(4)

driver.find_element(By.CLASS_NAME, "css-47sehv").click()


names = []
scores = []
genress = []
anime_to_watch = []

while True:
    try:
        i = 0
        for i in range(0, 50):
            time.sleep(1) 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        find = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='media-card']/a[@class='cover']")))
        
        anime_links = [link.get_attribute("href") for link in find]

        for anime_link in anime_links:
            time.sleep(1)

            driver.get(anime_link)

            time.sleep(1)
            name = driver.find_element(By.XPATH,  "//div[@class='content']/h1")
            print(name.text)
            names.append(name.text)
            avarege_score = driver.find_element(By.XPATH,  "//div[@class='el-tooltip data-set']")
            score = avarege_score.find_element(By.XPATH, "//div[@class='el-tooltip data-set']//div[@class='value']")
            score_text = score.text
            score_num = score_text.replace('%', '')
            print(score_num)
            scores.append(score_num)
            genres_ = avarege_score.find_element(By.XPATH, "//div[@class='data-set data-list']//div[@class='type'][contains(text(), 'Genres')]")
            genres = genres_.find_elements(By.XPATH, "following-sibling::div//a")
            for genre in genres:
                print(genre.text)
                genress.append(genre.text)
                if "Fantasy" in genre.text:
                    if int(score_num) > 75 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)
                elif "Action" in genre.text:
                    if int(score_num) > 85 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)
                elif "Romance" in genre.text:
                    if int(score_num) > 80 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)
                elif "Slice of Life" in genre.text:
                    if int(score_num) > 78 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)
                elif "Slice of Life" in genre.text:
                    if int(score_num) > 78 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)
                elif "Psychological" in genre.text:
                    if int(score_num) > 82 :
                        if name.text not in anime_to_watch:
                            anime_to_watch.append(name.text)
                            print(anime_to_watch)

            driver.back()
            time.sleep(2) 
    except NoSuchElementException:
        print("No more anime to scrape.")
        break
driver.quit()