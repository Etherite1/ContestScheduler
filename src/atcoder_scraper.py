from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

def scrape():
    url = "https://atcoder.jp/contests"
    op = Options()
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=op)
    driver.get(url)

    ac_content = BeautifulSoup(driver.page_source, 'lxml')

    upcoming_contests = ac_content.find("div", id = "contest-table-upcoming")
    tbody = upcoming_contests.find("tbody")
    contestDict = {}
    for idx, contest in enumerate(tbody.find_all("tr")):
        current_dict = {}

        tds = contest.find_all("td")
        timestr = tds[0].getText()
        timestr = timestr[:10] + timestr[16:]
        dt = datetime.strptime(timestr, "%Y-%m-%d%H:%M").astimezone(tz = timezone.utc)
        current_dict['site'] = "AC"
        current_dict['name'] = tds[1].find("a").getText()
        current_dict['time'] = dt.strftime("%Y-%m-%d %H:%M")
        
        contestDict[idx] = current_dict
        
    return contestDict

def run():
    try:
        return scrape()
    except Exception as e:
        print(__file__, "is broken")
        print(e)
        return {}