from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta, timezone
import json

def scrape():
    url = "https://codeforces.com/contests"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
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
        name = cols[0].getText().strip();
        time = (cols[2].getText().strip()[0:cols[2].getText().strip().index("UTC")])
        dt = datetime.strptime(time, "%b/%d/%Y %H:%M").astimezone(tz = timezone.utc)
        countdown = int((dt - datetime.now(tz = timezone.utc)).total_seconds())

        currentDict['site'] = "CF"
        currentDict['name'] = name
        currentDict['time'] = dt.strftime("%b/%d/%Y %H:%M")
        currentDict['countdown'] = str(countdown)

        contestDict[idx] = currentDict

    return contestDict