from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
import time as time_library

def scrape():
    time_library.sleep(5)
    url = "https://codeforces.com/contests?complete=true"
    op = Options()
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=op)
    driver.get(url)

    cf_content = BeautifulSoup(driver.page_source, 'lxml')
    contest_flex_div = cf_content.find('div', class_='contestList')

    datatable = contest_flex_div.find("div", class_ = "datatable")

    table = datatable.find("table")

    contests = table.select("tr[data-contestid]")

    contestDict = {}
    for idx, contest in enumerate(contests):
        currentDict = {}
        cols = contest.find_all("td")
        unwanted = cols[0].find("a")
        if(unwanted != None):
            unwanted.extract()
        name = cols[0].getText().strip()
        time = str(cols[2].getText().strip())
        utc_idx = time.find("UTC")
        if utc_idx != -1:
            time = time[:utc_idx]
        dt = datetime.strptime(time, "%b/%d/%Y %H:%M").astimezone(tz = timezone.utc)
        countdown = int((dt - datetime.now(tz = timezone.utc)).total_seconds())

        currentDict['site'] = "CF"
        currentDict['name'] = name        
        currentDict['time'] = dt.strftime("%Y-%m-%d %H:%M")
        currentDict['countdown'] = str(countdown)

        contestDict[idx] = currentDict

    return contestDict