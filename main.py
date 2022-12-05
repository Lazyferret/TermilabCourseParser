import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import sqlite3

f = open("IT_Essentials.json", encoding='utf-8', mode='r')
data = json.load(f)
data_back = data.copy()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get("https://lms.termilab.ru/login")
time.sleep(5)
email_input = driver.find_element(By.ID, "email")
email_input.clear()
email_input.send_keys("bondarev.a.p@edu.mirea.ru")
time.sleep(3)
password_input = driver.find_element(By.ID, "password")
time.sleep(2)
password_input.clear()
password_input.send_keys("GtJMq!VpkZsG3!2")
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(7)
try:
    for i in data.keys():
        for j in data[i].keys():
            url = data[i][j]
            print(url)
            driver.get(url)
            time.sleep(2)
            sources = driver.find_elements(By.TAG_NAME, "source")
            sources_urls = []
            for k in sources:
                sources_urls.append(k.get_attribute("src"))
            data_back[i][j] = sources_urls
            time.sleep(random.randint(1, 5))

            # WebDriverWait(driver, timeout=50)

except Exception as ex:
    print("exception!", ex)
finally:
    with open("IT_Essentials_static.json", "w") as outfile:
        json.dump(data_back, outfile, sort_keys=False, ensure_ascii=False)
    #    pass
    driver.close()
    driver.quit()
