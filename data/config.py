import os

RAPID_API_KEY = os.environ.get('RAPID_API_KEY', 'your_default_key_here')

headers = {
    'x-rapidapi-key': RAPID_API_KEY,
    'x-rapidapi-host': "free-api-live-football-data.p.rapidapi.com"
}

leagues = {
    "Champions League": 42,
    "Premier League": 47,
    "La Liga": 87,
    "Europa League": 67,
    "Serie A": 55,
    "Bundesliga": 54,
    "Ligue 1": 53
}

rss_feeds = [
    "https://www.eyefootball.com/rss_news_main.xml",
    "https://www.espn.com/soccer/story/_/id/37380404/rss",
    "https://footballaction.co.uk/feed",
    "https://livesoccerupdates.com/feed/"
]
