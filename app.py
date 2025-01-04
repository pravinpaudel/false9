import streamlit as st
from components.home import show_home
from components.fixtures import show_fixtures
from components.standings import show_standings
from data.config import leagues
from streamlit_navigation_bar import st_navbar

# page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
# st.write(page)

st.set_page_config(page_title="False-9", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Matches", "Standings"), index=0)

if "selected_league" not in st.session_state:
    st.session_state.selected_league = "Premier League"  # Default league

if page == "Home":
    show_home()
elif page == "Matches":
    show_fixtures()
elif page == "Standings":
    st.header("Standings")
    league_names = list(leagues.keys())
    # Create columns for horizontal layout
    cols = st.columns(len(league_names))  # One column per league button
    for idx, league_name in enumerate(league_names):
        with cols[idx]:
            if st.button(league_name):
                st.session_state.selected_league = league_name
                
    show_standings(st.session_state.selected_league)
