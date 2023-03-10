from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta
from github_setting import get_github_repo, upload_github_issue


def extract_commit_data():
    upload_contents = ''

    for i in range(len(member)):
        link = '\"' + url + member[i] + '\"'
        name = names[i]
        st = streak[i]
        tier = tiers[i]
        rank = ranks[i]
        content = f"<a href={link}>" + name + "    " + "</a>" + tier + "<br/>"
        content += "<blockquote data-ke-style=\"style2\">" + st + "<br/>" + rank + "등</blockquote><br/>"
        upload_contents += content

    return upload_contents


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "ABLT_MEMBER"
    now = date.today()
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
    
    '''
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    '''
    chrome_driver = os.path.join('chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    # driver 실행

    url = 'https://solved.ac/'
    driver.get(url)
    member = ['dhalsdl12','shgusgh12', 'shinsion', 'wns0865']
    names = ['권오민', '노현호', '신시온', '이준형']
    streak = ['현재 0일', '현재 0일', '현재 0일', '현재 0일', '현재 0일']
    tiers = []
    ranks = []
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
        tiers.append(tier)
        rank = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div/div[2]/div[1]/div[2]/b').text
        rank = rank[1:]
        rank = rank.replace(',', '')
        ranks.append(rank)
        print(names[i], solved)
        if day == 0:
            streak[i] = streak[i] + '  벌금입니다.'
        else:
            streak[i] = solved


    driver.close()
    
    issue_title = f"어제({yesterday}) 알고리즘 문제 풀었어?"
    upload_contents = extract_commit_data()
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")