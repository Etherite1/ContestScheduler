from flask import Flask
from flask_cors import CORS
import pandas as pd
import scrape_main
from multiprocessing import Process, Value

app = Flask(__name__)
CORS(app)

p = Process(target=scrape_main.run, args=[])
p.start()

@app.route("/")
def run():
    print("Flask server is running")
    df = pd.read_csv("data/contest_data.csv")
    df = df.drop(df.columns[0], axis = 1)
    return df.to_json(orient = "records")