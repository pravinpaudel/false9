import streamlit as st
from components.home import show_home
from components.fixtures import show_fixtures
from components.standings import show_standings
from data.config import leagues
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="False-9",
    page_icon="logo.png"
)

st.markdown(""" 
    <style> 
        header {
        visibility: hidden;
        display: none;
        } 
        .stMainBlockContainer {
        padding-top: unset;
        }
    </style> """, unsafe_allow_html=True)

# Display the logo above the navigation bar 
st.image("logo.png", width=100) 
#logo = st.logo(image="logo.png", size="large", icon_image="logo.png")

page = option_menu(
    menu_title = None, # Required
    options = ["Home", "Matches", "Statistics"], # Required
    icons = ["house", "fan", "bar-chart"],
    default_index = 0, # Default page index
    orientation = "horizontal", # Optional  
)

#st.set_page_config(page_title="False-9", layout="wide")
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ("Home", "Matches", "Standings"), index=0)

if "selected_league" not in st.session_state:
    st.session_state.selected_league = "Premier League"  # Default league

if page == "Home":
    show_home()
elif page == "Matches":
    show_fixtures()
elif page == "Statistics":
    league_names = list(leagues.keys())
    
    # Create a sidebar for league buttons 
    with st.sidebar: 
        for league_name in league_names: 
            if st.button(league_name): 
                st.session_state.selected_league = league_name

    show_standings(st.session_state.selected_league)
    # Create columns for horizontal layout
    # cols = st.columns(len(league_names))  # One column per league button
    # with st.sidebar:
    #     for idx, league_name in enumerate(league_names):
    #         with cols[idx]:
    #             if st.button(league_name):
    #                 st.session_state.selected_league = league_name
                
    
