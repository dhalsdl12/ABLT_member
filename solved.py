from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time, sys, os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
# driver 실행

url = 'https://solved.ac/'
driver.get(url)
member = ['dhalsdl12','shgusgh12', 'shinsion', 'wns0865']
name = ['권오민', '노현호', '신시온', '이준형']
for i in range(len(member)):
    driver.get(url + member[i])
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # category = soup.select('svg > rect')
    # /html/body/div[1]/div/div[4]/div/div[4]/div[3]/div[1]/svg/rect[1]
    # print(category[0])
    # solved = soup.select('svg > text')
    # /html/body/div[1]/div/div[4]/div/div[4]/div[1]/div[2]/div/div/div/b
    
    solved = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div/div[4]/div[1]/div[2]/div/div/div').text
    day = int(driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div/div[4]/div[1]/div[2]/div/div/div/b').text)
    print(name[i], solved)
    if day == 0:
        print('벌금입니다!')
    else:
        print('잘하고 있습니다.')