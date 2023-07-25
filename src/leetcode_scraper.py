from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def scrape():
    url = "https://leetcode.com/contest/"
    driver = webdriver.Chrome()
    driver.get(url)

    lc_content = BeautifulSoup(driver.page_source, 'lxml')
    contest_flex_div = lc_content.find('div', class_='swiper-wrapper')
    contests = contest_flex_div.find_all('a', class_='h-full w-full')
    for contest in contests:
        name = contest.find('div', class_='truncate').text
        time = contest.find('div', class_='flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2').text
        countdown = " ".join(contest.find('div', class_='flex items-center').text.split(" ")[2:])
        print(f'''Name: {name}\nTime: {time}\nStarts in: {countdown}\n''')

