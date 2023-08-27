from __future__ import print_function
from flask import Flask, jsonify
from flask_cors import CORS
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from datetime import datetime
import pytz
import os.path
import csv

import pandas as pd
import scrape_main

from multiprocessing import Process, Value
# from calendar import calendar_bp

app = Flask(__name__)
CORS(app)
# app.register_blueprint(calendar_bp)
p = Process(target=scrape_main.run, args=[])
p.start()

SCOPES = ['https://www.googleapis.com/auth/calendar']

@app.route("/") # only has one page
def run():
    print("Flask server is running")
    df = pd.read_csv("data/contest_data.csv")
    df = df.drop(df.columns[0], axis = 1)
    return df.to_json(orient = "records")

'''
@app.route('/api/calendar/<site>', methods=['GET','POST'])
def update_events(site): # the first call to update_events will handle auth
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first 
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=59474)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds) # service endpoint

        # Call the Calendar API
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # list only contains contests from <site>
        events_result = service.events().list(calendarId='primary', kind=site, timeMin=now, orderBy='startTime').execute()
        events = events_result.get('items', [])
        calendar = service.calendars().get(calendarId='primary').execute() # this is so we can get the timezone of the user

        if events: # events has elements (checkbox was unchecked) -> delete all events in list
            for event in events:
                service.events().delete(calendarId='primary', eventId=event['id']).execute()
        else: # events is empty (checkbox was checked) -> insert site events
            with open("data/contest_data.csv") as csv_file:
                reader = csv.DictReader(csv_file)
                for contest in reader[1:]: # row in csv file, skip header
                    utc_start = datetime.strptime(contest['time'], '"%Y-%m-%d %H:%M"') # utc time
                    utc_end = utc_start + datetime.timedelta(minutes=60) 
                    event = {
                        'kind': site,
                        'summary': contest['name'],
                        'start': utc_start.astimezone(pytz.timezone(calendar['timezone'])), # convert to user local time
                        'end': utc_end.astimezone(pytz.timezone(calendar['timezone']))
                    }
                    service.events().insert(calendarId='primary', body=event).execute()
            pass
    except HttpError as error:
        print('An error occurred: %s' % error)
'''
if __name__ == '__main__':
    app.run();