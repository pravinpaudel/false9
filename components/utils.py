import http.client
import json
from data.config import RAPID_API_KEY, headers, leagues
from datetime import date

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
