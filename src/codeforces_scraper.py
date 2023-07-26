from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta, timezone

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
    for contest in contests:
        cols = contest.find_all("td")
        name = cols[0].getText().strip();
        time = (cols[2].getText().strip()[0:cols[2].getText().strip().index("UTC")])
        dt = datetime.strptime(time, "%b/%d/%Y %H:%M").astimezone(tz = timezone.utc)
        dt = dt.strftime("%b/%d/%Y %H:%M")
        
        print(f"Name: {name}")
        print(f"Time in UTC: {dt}\n")