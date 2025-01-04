import feedparser
import requests
import streamlit as st
import http.client
import json
from datetime import date
import os
import pandas as pd

# Replace this with secure storage (like environment variables or a secrets manager)
RAPID_API_KEY = os.environ['RAPID_API_KEY']
print("Check")
st.header("False-9")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Matches", "Standings"), index=0)

# List of RSS feed URLs
rss_feeds = [
    "https://news.google.com/rss/search?q=football",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.bbci.co.uk/news/rss.xml"
]

headers = {
    'x-rapidapi-key': RAPID_API_KEY,
    'x-rapidapi-host': "free-api-live-football-data.p.rapidapi.com"
}

# Fetch and parse the RSS feeds
def show_home():
    articles = []
    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                #"summary": entry.get("summary", "No summary available")
            })

    st.title("News Aggregator")
    for article in articles:
        st.header(article["title"])
        st.write(f"[Read more]({article['link']})")

# Display live football scores
def show_fixtures():
    st.header("Live Football Scores")
    matches = fetch_live_scores()
    if not matches:
        st.write("No matches found or API error occurred.")
        return
    print(matches)
    for match in matches['response']['matches']:
        hometeam = match['home']['name']
        awayteam = match['away']['name']
        homeScore = match['home'].get('score', 0)
        awayScore = match['away'].get('score', 0)
        status = match['status'].get('finished', False)
        st.subheader(f"{hometeam} vs {awayteam}")
        st.write(f"Score: {homeScore} - {awayScore}")
        st.write(f"Status: {'Finished' if status else 'Ongoing'}")

# Function to fetch live football scores
def fetch_live_scores():
    try:
        conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
        
        today = date.today().isoformat()
        today = today.replace("-", "")
        conn.request("GET", f"/football-get-matches-by-date?date={today}", headers=headers)
        res = conn.getresponse()
        if res.status != 200:
            st.error("Failed to fetch data from the API.")
            return None
        data = res.read()
        matches = json.loads(data.decode("utf-8"))
        return matches
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


leagues = {
    "Champions League": 42,
    "Premier League": 47,
    "La Liga": 87,
    "Europa League" : 67, 
    "Serie A": 55,
    "Bundesliga": 54,
    "Ligue 1": 53
}


def show_standings(league_name):
    league_id = leagues[league_name]
    conn = http.client.HTTPSConnection("free-api-live-football-data.p.rapidapi.com")
    conn.request("GET", f"/football-get-standing-all?leagueid={league_id}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    table = json.loads(data.decode("utf-8"))
    # Extract the relevant part of the JSON 
    standing_data = table['response']['standing']
    #logo = st.logo("url")
    
    # Convert to DataFrame 
    df = pd.DataFrame(standing_data, columns=['idx', 'name', 'played', 'wins', 'draws', 'losses', 'scoresStr', 'goalConDiff', 'pts'])
    df.columns = ['Rank', 'Name', 'Played', 'Wins', 'Draws', 'Losses', 'Scores', 'Goal Difference', 'Points']
    st.table(df.style.hide(axis="index"))


if "selected_league" not in st.session_state:
    st.session_state.selected_league = "Premier League"  # Default league
    
if page == "Home":
    show_home()
elif page == "Matches":
    show_fixtures()
elif page == "Standings":
    st.header("Standings")
    # Display buttons for different leagues
    league_names = list(leagues.keys())
    for league_name in league_names:
        if st.button(league_name):
            st.session_state.selected_league = league_name

    # Show standings for the selected league
    show_standings(st.session_state.selected_league)


if st.session_state.get("page") == "Standings":
    st.header("Standings")

    

#show_home()




