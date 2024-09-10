import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options




all_news_dict= []
chrome_options = Options()

# Download the ChromeDriver executable from https://chromedriver.chromium.org/downloads
service = Service(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver-win64/chromedriver.exe")


url = "https://akharinkhabar.ir/"

for group in ["sport", "cinema", "money"]:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(f"{url}/{group}")

    try:
        news_list = driver.find_elements( By.CSS_SELECTOR, ".rectangle_container__rBE5L")

    # for link in driver.find_elements(By.CSS_SELECTOR, ".rectangle_image_container__OCyhG a"):
    #     try:
    #         link = link.get_attribute("href")
    #         driver.get(link)
    #     except:
    #         pass

        for news in news_list:
            my_list = news.text.split("\n")
            news_dict = {
                "group": my_list[0],
                "time" : my_list[2],
                "title" : my_list[3],
                "like": my_list[4],
                "comments": my_list[5],
                "view": my_list[6],
            }
            all_news_dict.append(news_dict)


    finally:
        driver.close()

import pandas as pd
df = pd.DataFrame(all_news_dict)
# choose your path 
df.to_excel("F:\\DA\\DA 07\\DA 07\\news1.xlsx", index=False)