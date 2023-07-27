from flask import Flask
from flask_cors import CORS
import scrape_main
import pandas as pd


app = Flask(__name__)
CORS(app)

@app.route("/")
def run():
    df = pd.read_csv("data/contest_data.csv")
    df = df.drop(df.columns[0], axis = 1)
    return df.to_json(orient = "records")