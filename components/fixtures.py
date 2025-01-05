import streamlit as st
from components.utils import fetch_fixtures, fetch_fixture_details, fetch_live_scores


def show_fixtures():
    #st.header("Today's Fixtures ")
    #fixtures = fetch_live_scores()
    fixtures = fetch_fixtures()
    if not fixtures:
        st.write("No matches today.")
        return

    for league in fixtures:
        # League Name
        st.html(
            f"<h1 style='text-align: center;'><span style='color: #FA7F73;'> {league['name']} </span></span></h1>"
        )
        
        #st.subheader(f"\t{league['name']}")
        
        for match in league['matches']:
            event_id = match['id']
            time = match['time']
            
            home_team = match['home']['name']
            away_team = match['away']['name']
            home_score = match['home']['score']
            away_score = match['away']['score']

            match_day = match['tournamentStage']

            try:
                live_time = match['status'].get('liveTime')['short']
            except Exception as e:
                live_time = -1

            status = match['status']['finished']
            # try:
            #     status = match['status']['finished']
            # except Exception as e:
            #     st.write(e)
            #     status = False

            if not status:
                st.html(
                    f"<h1 style = 'margin: 0;'>{home_team}  <span style='color: yellow;'>{home_score} - {away_score}</span>   \
                    {away_team} \t > <span style='color: yellow;'>{live_time}</span></h1>"
                )
            else:
                st.html(f"<h1 style = 'margin: 0;'>{home_team}  <span style='color: #FA7F73;'>{home_score} - {away_score}</span>    {away_team}</h1>")
                
            #st.write(f"Status: {'Finished' if status else 'Ongoing'}")
            st.write(f"\tDate & Time: {time}")
            st.write(f"Matchday: {match_day}")

            # Popover for detailed match info
            with st.popover("View Details", icon=":material/expand_circle_down:", disabled=False): 
                home_team_info, away_team_info = fetch_fixture_details(event_id)
                st.json(home_team_info)
                st.json(away_team_info)

            st.write("---")
            
    # for match in fixtures['response']['matches']:
    #     home_team = match['home']['name']
    #     away_team = match['away']['name']
    #     home_score = match['home'].get('score', 0)
    #     away_score = match['away'].get('score', 0)
    #     status = match['status'].get('finished', False)
    #     st.subheader(f"{home_team} vs {away_team}")
    #     st.write(f"Score: {home_score} - {away_score}")
    #     st.write(f"Status: {'Finished' if status else 'Ongoing'}")
