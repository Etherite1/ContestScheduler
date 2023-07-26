from flask import Flask
from flask_cors import CORS
import json

from src import leetcode_scraper
from src import codeforces_scraper

app = Flask(__name__)
CORS(app)

@app.route("/")
def scrape():
    # leetcode_scraper.scrape()
    return json.dumps(codeforces_scraper.scrape())