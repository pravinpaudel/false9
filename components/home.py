import streamlit as st
import feedparser
from data.config import rss_feeds

def show_home():
    st.title("Kick-Off")
    articles = []
    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
            })
    for article in articles:
        st.header(article["title"])
        st.write(f"[Read more]({article['link']})")
