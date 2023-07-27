import json
import time
import pandas as pd
import os

from src import leetcode_scraper
from src import codeforces_scraper

def scrape():
    contests = [] # stores a bunch of dictionaries - contests[i] represents one (1) contest

    codeforces_dict = codeforces_scraper.scrape()
    for codeforces_contest in codeforces_dict.values():
        contests.append(codeforces_contest)

    leetcode_dict = leetcode_scraper.scrape()
    for leetcode_contest in leetcode_dict.values():
        contests.append(leetcode_contest)

    if(not os.path.isdir("data")):
       os.makedirs("data")

    contest_df = pd.DataFrame(contests)
    contest_df.to_csv("data/contest_data.csv")

while(True):
    scrape()
    time.sleep(300)