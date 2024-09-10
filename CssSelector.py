import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://accounts.google.com/"

driver = webdriver.Chrome()
driver.get(url)

# wait = WebDriverWait(driver, 30)
# wait.until(EC.)

email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email.send_keys("ericksmith.a@gmail.com")


btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
btn.click()




driver.close()