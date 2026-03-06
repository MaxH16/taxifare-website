import streamlit as st
import datetime
import pandas as pd
import numpy as np



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
pickup_latitude_input = st.text_input('Pickup latitude', '40.7128')
pickup_longitude_input = st.text_input('Pickup longitude', '-74.0060')

pickup_latitude = float(pickup_latitude_input)
pickup_longitude = float(pickup_longitude_input)

st.write('You will be picked up at', pickup_latitude,',', pickup_longitude)

# df_pickup = pd.DataFrame({'lat': [pickup_latitude], 'lon': [pickup_longitude]})
# st.map(df_pickup)

'''
## Enter your dropoff coordinates
'''
dropoff_latitude_input = st.text_input('Dropoff latitude', '40.7306')
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
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
