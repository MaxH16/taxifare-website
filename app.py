import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests

import streamlit as st

def local_css():
    st.markdown("""
    <style>
    /* Changement du fond de l'application */
    .stApp {
        background-image: url("https://bonpourtoi.ca/app/uploads/2020/04/BPT-Article-biere-tinyjpg.jpeg");
        background-attachment: fixed;
        background-size: cover;
    }

    /* Personnalisation des titres */
    h1, h2, h3 {
        color: #FFCD00 !important; /* Jaune Drapeau Belge */
        font-family: 'Helvetica Neue', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 3px solid #E30613; /* Ligne rouge sous les titres */
        padding-bottom: 10px;
    }

    /* Style des boutons (Le bouton "Estimate Fare" sera Rouge) */
    .stButton>button {
        background-color: #E30613 !important; /* Rouge Drapeau Belge */
        color: white !important;
        border-radius: 20px !important;
        border: 2px solid #FFCD00 !important;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #FFCD00 !important;
        color: black !important;
        transform: scale(1.02);
    }

    /* Style des inputs */
    .stTextInput>div>div>input {
        background-color: #333333;
        color: #FFCD00 !important;
        border: 1px solid #E30613 !important;
    }

    /* La petite touche : bordure de la page aux couleurs du drapeau */
    header {
        border-top: 10px solid #000000;
        border-bottom: 5px solid #FFCD00;
    }

    /* Footer ou Sidebar */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 5px solid #E30613;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- Contenu de ton app ---
st.title("🇧🇪 Belgian Taxi Fare Predictor")
'''
## Bienvenue une fois ! Calcule le prix de ta course entre deux pintes.
'''

'''
## Select the date and time you want to be picked up
'''
col1, col2 = st.columns(2)
with col1:
    d = st.date_input(
        "Select your pickup day",
        datetime.date(2025, 7, 6))
with col2:
    t = st.time_input('Select an hour of pickup', datetime.time(8, 45))

st.write('Your pickup is scheduled on', d, 'at', t, 'sharp !')

'''
## Enter your pickups coordinates
'''
col1, col2 = st.columns(2)
with col1:
    pickup_latitude_input = st.text_input('Pickup latitude', '40.7128')
with col2:
    pickup_longitude_input = st.text_input('Pickup longitude', '-74.0060')

pickup_latitude = float(pickup_latitude_input)
pickup_longitude = float(pickup_longitude_input)

st.write('You will be picked up at', pickup_latitude,',', pickup_longitude)

# df_pickup = pd.DataFrame({'lat': [pickup_latitude], 'lon': [pickup_longitude]})
# st.map(df_pickup)

'''
## Enter your dropoff coordinates
'''
col1, col2 = st.columns(2)
with col1:
    dropoff_latitude_input = st.text_input('Dropoff latitude', '40.7306')
with col2:
    dropoff_longitude_input = st.text_input('Dropoff longitude', '-73.9352')

dropoff_latitude = float(dropoff_latitude_input)
dropoff_longitude = float(dropoff_longitude_input)

st.write('You will be dropped off at', dropoff_latitude,',', dropoff_longitude)

# df_dropoff = pd.DataFrame({'lat': [dropoff_latitude], 'lon': [dropoff_longitude]})
# st.map(df_dropoff)

df_trip = pd.DataFrame({
            'lat': [pickup_latitude, dropoff_latitude],
            'lon': [pickup_longitude, dropoff_longitude]
        })

st.map(df_trip)

'''
## Enter the amount of passengers for the ride
'''
passenger_num = st.number_input('Number of passengers', min_value = 1, max_value = 8,)

st.write('Your ride will feature ', passenger_num, ' passenger(s)')


params = {
    "pickup_datetime": f"{d} {t}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_num
}

url = 'https://taxifare.lewagon.ai/predict'

if st.button('Estimate Fare'):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # --- 4. Récupération de la prédiction ---
        prediction = response.json().get('fare', "Error")

        # ## Affichage du résultat
        st.success(f"### The estimated fare is: ${prediction:.2f}")
    else:
        st.error("Could not connect to the API. Please check your parameters or URL.")

if st.button('Click here to enjoy your ride !'):
    st.balloons()
