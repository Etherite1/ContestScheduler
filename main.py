from flask import Flask
import json

from src import leetcode_scraper
from src import codeforces_scraper

app = Flask(__name__)

@app.route("/")
def scrape():
    # leetcode_scraper.scrape()
    return json.dumps(codeforces_scraper.scrape());