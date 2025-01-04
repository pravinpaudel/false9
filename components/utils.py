import http.client
import json
from data.config import RAPID_API_KEY, headers, leagues
from datetime import date

def fetch_live_scores():
    try:
        conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
        today = date.today().isoformat().replace("-", "")
        conn.request("GET", f"/football-get-matches-by-date?date={today}", headers=headers)
        res = conn.getresponse()
        if res.status != 200:
            return None
        data = res.read()
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
