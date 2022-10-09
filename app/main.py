import streamlit as st

from utils import head, body, teams, locations

import pickle
model = pickle.load(open('model/gaussian_nba.pkl', 'rb'))

team, opp, loc = head()

if st.button('Predict!'):
    str_hasil = "pilihlah team dan opponent yang berbeda"

    if (team != opp):
        prediction = model.predict([[teams.index(team), teams.index(opp), locations.index(loc)]])[0]

        output = {0: 'Lose', 1: 'Win'}
        
        str_hasil = (team + " vs " 
                    + opp + " ar "
                    + loc + " prediction leans to: "
                    + str(output[prediction])
                    )

    body(str_hasil)