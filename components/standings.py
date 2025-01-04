import streamlit as st
import pandas as pd
from components.utils import fetch_standings

def show_standings(league_name):
    standings = fetch_standings(league_name)
    if not standings:
        st.error("Unable to fetch standings.")
        return
    df = pd.DataFrame(standings, columns=['idx', 'name', 'played', 'wins', 'draws', 'losses', 'scoresStr', 'goalConDiff', 'pts'])
    df.columns = ['Rank', 'Name', 'Played', 'Wins', 'Draws', 'Losses', 'Scores', 'Goal Difference', 'Points']
    
    st.table(df.style.hide(axis="index"))
