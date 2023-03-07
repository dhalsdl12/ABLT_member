from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time, sys, os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
# driver 실행

url = 'https://solved.ac/'
member = ['dhalsdl12']
for i in range(len(member)):
    driver.get(url + member[i])
    driver.refresh()
    time.sleep(5)

    solved = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[5]/div/div[4]/div[3]/div[1]/svg/rect[1]')
    print(solved)
    solved.click()

    check = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[5]/div/div[4]/div[3]/div[1]/svg/text[13]')
    print(check.text)

    time.sleep(10)