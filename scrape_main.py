import json
import time
import pandas as pd
import os

from src import leetcode_scraper, codeforces_scraper, codechef_scraper, atcoder_scraper

def scrape():
    print("scraping :)")
    contests = [] # stores a bunch of dictionaries - contests[i] represents one (1) contest

    codeforces_dict = codeforces_scraper.run()
    for codeforces_contest in codeforces_dict.values():
        contests.append(codeforces_contest)

    leetcode_dict = leetcode_scraper.run()
    for leetcode_contest in leetcode_dict.values():
        contests.append(leetcode_contest)

    codechef_dict = codechef_scraper.run()
    for codechef_contest in codechef_dict.values():
        contests.append(codechef_contest)

    atcoder_dict = atcoder_scraper.run()
    for atcoder_contest in atcoder_dict.values():
        contests.append(atcoder_contest)

    if(not os.path.isdir("data")):
       os.makedirs("data")

    contest_df = pd.DataFrame(contests)
    contest_df.to_csv("data/contest_data.csv")

    print("scraped :)", flush = True)

def run():
    while(True):
        scrape()
        time.sleep(60)