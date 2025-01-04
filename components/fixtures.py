import streamlit as st
from components.utils import fetch_live_scores

def show_fixtures():
    st.header("Live Football Scores")
    matches = fetch_live_scores()
    if not matches:
        st.write("No matches found or API error occurred.")
        return
    for match in matches['response']['matches']:
        home_team = match['home']['name']
        away_team = match['away']['name']
        home_score = match['home'].get('score', 0)
        away_score = match['away'].get('score', 0)
        status = match['status'].get('finished', False)
        st.subheader(f"{home_team} vs {away_team}")
        st.write(f"Score: {home_score} - {away_score}")
        st.write(f"Status: {'Finished' if status else 'Ongoing'}")
