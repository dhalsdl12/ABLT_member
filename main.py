from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta


def pageCrawl():
    html = drive.page_source
    soup = BeautifulSoup(html, 'html.parser')

    category = soup.select('svg > g > g > rect')

    for a in category:
        d = a.attrs['data-date']
        if d == yesterday:
            commit = a.text.split()[0]
            print(d, ":", commit)


now = date.today()
yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
team = ['dhalsdl12', 'seokiis', 'shgusgh12', 'wns0865']
url = 'https://github.com/'
driver = 'C:\\Users\\dhals\\Downloads\\chromedriver.exe'

drive = webdriver.Chrome(driver)
for i in range(4):
    drive.get(url+team[i])
    print(team[i])
    pageCrawl()
drive.close()
