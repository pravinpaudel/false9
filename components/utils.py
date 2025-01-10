import http.client
import json
#from data.config import headers, leagues
from datetime import date

import os
import requests
API_KEY = os.environ.get('APISPORTS_API_KEY')
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

def fetch_live_scores():
    try:
        # Create an HTTPS connection to the specifed host ie.. free-api ...
        conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")

        # Create a date object for today
        today = date.today().isoformat().replace("-", "")

        # Send an HTTP GET request to the API endpoint
        conn.request("GET", f"/football-get-matches-by-date?date={today}", headers=headers)

        # Get the response from the API
        res = conn.getresponse()

        if res.status != 200:
            return None

        # Read the response data
        data = res.read()
        
        # Decode method is used to convert the byte data received from the HTTP response into a string using UTF-8 encoding. When we receive a data from an HTTP response, it is in the form of bytes. We need to convert it into a string using the decode method.
        # The json.loads() method is used to convert the string data into a Python dictionary.
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        return None

def fetch_standings(league_name):
    try:
        league_id = leagues[league_name]
        conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
        conn.request("GET", f"/football-get-standing-all?leagueid={league_id}", headers=headers)
        res = conn.getresponse()
        if res.status != 200:
            return None
        data = res.read()
        standings = json.loads(data.decode("utf-8"))['response']['standing']
        return standings
    except Exception as e:
        return None

# def fetch_news():
#     conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
#     conn.request("GET", "/football-get-trendingnews", headers=headers)

#     res = conn.getresponse()
#     data = res.read()
#     news = json.loads(data.decode("utf-8"))['response']['news']
#     print(news)


#fetch_news()

def fetch_fixtures():
    try:
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        
        conn.request("GET", "/fixtures?date=2025-01-10&live=39-140", headers=headers)

        res = conn.getresponse()

        if res.status != 200:
            return None
        data = res.read()
        
        fixtures = json.loads(data.decode("utf-8"))['response']
        print(fixtures)
        
        return fixtures
    except Exception as e:
        return None

def fetch_fixture_details(event_id):
    try:
        conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
        conn.request("GET", f"/football-get-awayteam-lineup?eventid={event_id}", headers=headers)

        res = conn.getresponse()
        data = res.read()

        away_team_info = json.loads(data.decode("utf-8"))['response']

        conn.request("GET", f"/football-get-hometeam-lineup?eventid={event_id}", headers=headers)

        res = conn.getresponse()
        data = res.read()
    
        home_team_info = json.loads(data.decode("utf-8"))['response']

        return home_team_info, away_team_info
        
    except Exception as e:
        return None, None


def fetch_standing(league_id):
    
    api_call = requests.get("https://www.thesportsdb.com//api/v1/json/3/lookuptable.php?l=4328&s=2024-2025")
    storage = api_call.json()
        
    for event in storage["events"]:
        date_event = event["dateEvent"]
        home_team = event["strHomeTeam"]
        away_team = event["strAwayTeam"]

        print(f"{date_event}: {home_team} vs {away_team}")

event_ids = [2052711, 2052712, 2052713, 2052714]

