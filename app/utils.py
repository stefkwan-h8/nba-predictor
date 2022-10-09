import streamlit as st
    
teams = ['ANA', 'AND', 'ATL', 'BAL', 'BLB', 'BOS', 'BRK', 'BUF', 'CAP',
            'CAR', 'CHA', 'CHH', 'CHI', 'CHO', 'CHP', 'CHS', 'CHZ', 'CIN',
            'CLE', 'CLR', 'DAL', 'DEN', 'DET', 'DLC', 'DNA', 'DNN', 'DNR',
            'DTF', 'FLO', 'FTW', 'GSW', 'HOU', 'HSM', 'INA', 'IND', 'INJ',
            'INO', 'KCK', 'KCO', 'KEN', 'LAC', 'LAL', 'LAS', 'MEM', 'MIA',
            'MIL', 'MIN', 'MLH', 'MMF', 'MMP', 'MMS', 'MMT', 'MNL', 'MNM',
            'MNP', 'NJA', 'NJN', 'NOB', 'NOH', 'NOJ', 'NOK', 'NOP', 'NYA',
            'NYK', 'NYN', 'OAK', 'OKC', 'ORL', 'PHI', 'PHO', 'PHW', 'PIT',
            'POR', 'PRO', 'PTC', 'PTP', 'ROC', 'SAA', 'SAC', 'SAS', 'SDA',
            'SDC', 'SDR', 'SDS', 'SEA', 'SFW', 'SHE', 'SSL', 'STB', 'STL',
            'SYR', 'TEX', 'TOR', 'TRH', 'TRI', 'UTA', 'UTS', 'VAN', 'VIR',
            'WAS', 'WAT', 'WSA', 'WSB', 'WSC']
locations = ["Away", "Home", "Neutral"]

def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Predict winner of NBA Match
        </h1>
    """, unsafe_allow_html=True
    )
    
    st.caption("""
        <p style='text-align: center'>
        using gaussian naive bayes model built with sklearn, data from 
        <a href='https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-nba-elo-dataset'>FiveThirtyEight Kaggle</a>
        </p>
    """, unsafe_allow_html=True
    )

    team = st.selectbox("Team", teams, index=0)
    opp = st.selectbox("Opponent", teams, index=1)
    loc = st.selectbox("Location", locations, index=0)

    return team, opp, loc

def body(result):
    st.write(result)
    st.markdown('---')
