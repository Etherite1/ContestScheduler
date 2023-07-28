from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
import time

def scrape():
    url = "https://www.codechef.com/contests"
    op = Options()
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=op)
    driver.get(url)

    time.sleep(5)

    cc_content = BeautifulSoup(driver.page_source, 'lxml')
    # print(cc_content)

    contest_tables = cc_content.select('div[class*=_contest-tables]') # selects contest tables div
    upcoming_contests = contest_tables[0].select("div[class*=_table__container]")[1] # selects upcoming contests table from all table container divs
    contest_info = upcoming_contests.select('tr[data-testid]') # selects contest info for tr with data-testid attribute

    contestDict = {}
    for idx, contest in enumerate(contest_info):
        current_dict = {}
        cols = contest.findAll('td')
        current_dict['site'] = "CC"
        current_dict['name'] = cols[1].findAll("div")[1].getText()
        timestr = cols[2].findAll("div")[1].getText()
        timestr = timestr[:11] + timestr[15:]
        dt = datetime.strptime(timestr, "%d %b %Y%H:%M").astimezone(tz = timezone.utc)
        current_dict['time'] = dt.strftime("%Y-%m-%d %H:%M")
        countdown = int((dt - datetime.now(tz = timezone.utc)).total_seconds())
        current_dict['countdown'] = str(countdown)

        contestDict[idx] = current_dict

    return contestDict