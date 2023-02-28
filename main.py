import os
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta
from github_setting import get_github_repo, upload_github_issue


def extract_commit_data():
    upload_contents = ''

    for i in range(len(team)):
        link = '\"' + url + team[i] + '\"'
        name = team[i]
        commit = commits[i]
        penal = penalty[i]
        content = f"<a href={link}>" + name + "</a>" + "<br/>"
        content += "<blockquote data-ke-style=\"style2\">" + commit + "<br>" + penal + "</blockquote><br/>"
        upload_contents += content

    return upload_contents
    
    
def pageCrawl():
    html = drive.page_source
    soup = BeautifulSoup(html, 'html.parser')

    category = soup.select('svg > g > g > rect')

    for a in category:
        d = a.attrs['data-date']
        if d == yesterday:
            commit = a.text.split()[0]
            commits.append(str(d) + ' : ' + commit)
            if commit == 'No':
                penalty[i] = '경고! 공부하세요...'


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "KKNL_study"
    
    now = date.today()
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
    team = ['dhalsdl12', 'seokiis', 'shgusgh12', 'wns0865', 'Sion99']
    penalty = ['참 잘했어요!', '참 잘했어요!', '참 잘했어요!', '참 잘했어요!', '참 잘했어요!']
    commits = []
    url = 'https://github.com/'
    
    chrome_driver = os.path.join('chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    drive = webdriver.Chrome(chrome_driver, options=chrome_options)
    
    for i in range(5):
        drive.get(url+team[i])
        pageCrawl()

    for c in commits:
        print(c)

    drive.close()
    
    
    issue_title = f"어제({yesterday}) github commit 했어?"
    upload_contents = extract_commit_data()
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
