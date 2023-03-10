from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta


def extract_commit_data():
    upload_contents = ''

    for i in range(len(member)):
        link = '\"' + url + member[i] + '\"'
        name = names[i]
        st = streak[i]
        content = f"<a href={link}>" + name + "</a>" + "<br/>"
        content += "<blockquote data-ke-style=\"style2\">" + st + "</blockquote><br/>"
        upload_contents += content

    return upload_contents


if __name__ == "__main__":
    repository_name = "ABLT_MEMBER"
    now = date.today()
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    # driver 실행

    url = 'https://solved.ac/'
    driver.get(url)
    member = ['dhalsdl12','shgusgh12', 'shinsion', 'wns0865']
    names = ['권오민', '노현호', '신시온', '이준형']
    streak = ['현재 0일', '현재 0일', '현재 0일', '현재 0일', '현재 0일']

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
        tier = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div[1]/div[4]/span[2]/b').text
        rank = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div/div[2]/div[1]/div[2]/b').text
        rank = rank[1:]
        rank = rank.replace(',', '')
        print(rank)

    driver.close()
    