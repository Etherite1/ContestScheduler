from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

def scrape():
    url = "https://leetcode.com/contest/"
    op = Options()
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=op)
    driver.get(url)

    lc_content = BeautifulSoup(driver.page_source, 'lxml')
    contest_flex_div = lc_content.find('div', class_='swiper-wrapper')
    contests = contest_flex_div.find_all('a', class_='h-full w-full')
    contestDict = {}
    for idx, contest in enumerate(contests):
        current_dict = {}
        name = contest.find('div', class_='truncate').text
        time = contest.find('div', class_='flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2').text
        countdown = " ".join(contest.find('div', class_='flex items-center').text.split(" ")[2:])

        countdown_time = datetime.strptime(countdown, "%jd %Hh %Mm %Ss")
        countdown_timedelta = timedelta(days = countdown_time.day, hours = countdown_time.hour, minutes = countdown_time.minute, seconds = countdown_time.second);
        contest_time = datetime.now(tz = timezone.utc) + countdown_timedelta
        contest_time = roundTime(contest_time)
       
        current_dict['site'] = "LC"
        current_dict['name'] = name
        current_dict['time'] = contest_time.strftime("%Y-%m-%d %H:%M")

        contestDict[idx] = current_dict

    return contestDict


def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

def run():
    try:
        return scrape()
    except:
        print(__file__, "is broken")
        return {}