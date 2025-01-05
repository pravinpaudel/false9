import os

RAPID_API_KEY = os.environ.get('RAPID_API_KEY', 'your_default_key_here')

# Header to be used for all API requests, to authenticate the request 
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
    "https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/soccer,soccer/epl/league/1,soccer/mls/league/5,soccer/ucl/league/7,soccer/europa/league/8,soccer/wc/league/12,soccer/euro/league/13,soccer/wwc/league/14,soccer/nwsl/league/20,soccer/cwc/league/26,soccer/gold_cup/league/32,soccer/unl/league/67"
    "https://www.eyefootball.com/rss_news_main.xml",
    "https://www.espn.com/soccer/story/_/id/37380404/rss",
    "https://footballaction.co.uk/feed",
    "https://livesoccerupdates.com/feed/"
]
