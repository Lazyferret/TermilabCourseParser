import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import sqlite3
import itertools
def human_type(element, text):
    for char in text:
        time.sleep(random.randint(1,10)/15) #fixed a . instead of a ,
        element.send_keys(char)


with open("logpass.txt", mode='r') as f:
    login, password = f.read().split()

options = webdriver.ChromeOptions()
try:
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
except FileNotFoundError:
    driver = webdriver.Chrome()
driver.get("https://lms.termilab.ru/login")
time.sleep(5)
email_input = driver.find_element(By.ID, "email")
email_input.clear()
human_type(email_input, login)
time.sleep(3)
password_input = driver.find_element(By.ID, "password")
time.sleep(2)
password_input.clear()
human_type(password_input, password)
time.sleep(2)
driver.find_element(By.ID, "submit").click()
time.sleep(8)
courses = driver.find_elements(By.CLASS_NAME, "course-item")
data = {}
for course in courses:
    course_name = course.find_element(By.TAG_NAME, "h3").text.strip()
    print(course_name)
    course.find_element(By.CLASS_NAME, "enter-course").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "course-tabs").find_element(By.TAG_NAME, "a").click()
    time.sleep(3)
    chapter_accordion = driver.find_element(By.ID, "ui-accordion-accordion-panel-1")
    chapters = chapter_accordion.find_elements(By.TAG_NAME, "li")
    chapters_hrefs = [[chapter.find_element(By.TAG_NAME, "a").get_attribute("href"),chapter.find_element(By.TAG_NAME, "a").text.strip()] for chapter in chapters]
    for chapter, chapter_name in chapters_hrefs:
        chapter_data = {}
        driver.get(chapter)
        time.sleep(5)
        headers = [i.text.strip() for i in driver.find_elements(By.CLASS_NAME, "problem-header")]
        hrefs = [i.get_attribute("href") for i in driver.find_elements(By.CLASS_NAME, "link_lti_new_window")]
        for module in range(len(headers) - 1):
            # chapter_data[headers[module].text.strip()] = hrefs[module].get_attribute("href")
            driver.get(hrefs[module])
            time.sleep(3)
            sources = driver.find_elements(By.TAG_NAME, "source")
            sources_urls = []
            for source in sources:
                sources_urls.append(source.get_attribute("src"))
            chapter_data[headers[module]] = sources_urls
            time.sleep(random.randint(2, 6))
        data[chapter_name] = chapter_data
    driver.get("https://lms.termilab.ru/dashboard")
driver.close()
driver.quit()
with open("IT_Essentials_static.json", "w") as outfile:
    json.dump(data, outfile, sort_keys=False, ensure_ascii=False, indent=4)
    #    pass
