import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests

'''
# TaxiFare LeWagon
'''

st.markdown('''
Follow the instructions to request your ride !
''')

'''
## Select the date and time you want to be picked up
'''

d = st.date_input(
    "Select your pickup day",
    datetime.date(2019, 7, 6))

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

st.write('You will be picked up at', dropoff_latitude,',', dropoff_longitude)

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

url = 'https://taxifare.lewagon.ai/predict'


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
