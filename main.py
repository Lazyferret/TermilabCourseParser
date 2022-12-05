import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import sqlite3

with open("logpass.txt", mode='r') as f:
    login, password = f.read().split()

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get("https://lms.termilab.ru/login")
time.sleep(5)
email_input = driver.find_element(By.ID, "email")
email_input.clear()
email_input.send_keys(login)
time.sleep(3)
password_input = driver.find_element(By.ID, "password")
time.sleep(2)
password_input.clear()
password_input.send_keys(password)
time.sleep(2)
driver.find_element(By.ID, "submit").click()
time.sleep(8)
courses = driver.find_elements(By.CLASS_NAME, "course-item")
data = {}
for course in courses:
    print(course.find_element(By.TAG_NAME,"h3").text)
    """
    course.find_element(By.CLASS_NAME, "enter-course").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "course-tabs").find_element(By.TAG_NAME, "a").click()
    time.sleep(3)
    chapters = driver.find_element(By.ID, "ui-accordion-accordion-header-1").find_elements(By.TAG_NAME, "li")
    for chapter in chapters:
        driver.get(chapter.find_element(By.TAG_NAME, "a").get_attribute("href"))
        time.sleep(5)
        headers = driver.find_elements(By.CLASS_NAME, "problem-header")
        hrefs = driver.find_elements(By.CLASS_NAME, "link_lti_new_window")
        #data[course.find_element(By.TAG_NAME,"h3").]

    driver.close()
    driver.quit()

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
    driver.quit()"""

