import os

API_KEY = os.environ.get('APISPORTS_API_KEY')


# Header to be used for all API requests, to authenticate the request 
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

leagues = {
    "Champions League": 42,
    "Premier League": 39,
    "La Liga": 140,
    "Europa League": 67,
    "Serie A": 55,
    "Bundesliga": 54,
    "Ligue 1": 53,
    "Copa del Rey": 143
}

sports_db_leagues = {
    "Premier League": 4328
}

rss_feeds = [
    "https://api.foxsports.com/v2/content/optimized-rss?partnerKey=MB0Wehpmuj2lUhuRhQaafhBjAJqaPU244mlTDK1i&size=30&tags=fs/soccer,soccer/epl/league/1,soccer/mls/league/5,soccer/ucl/league/7,soccer/europa/league/8,soccer/wc/league/12,soccer/euro/league/13,soccer/wwc/league/14,soccer/nwsl/league/20,soccer/cwc/league/26,soccer/gold_cup/league/32,soccer/unl/league/67"
    "https://www.eyefootball.com/rss_news_main.xml",
    "https://www.espn.com/soccer/story/_/id/37380404/rss",
    "https://footballaction.co.uk/feed",
    "https://livesoccerupdates.com/feed/"
]
