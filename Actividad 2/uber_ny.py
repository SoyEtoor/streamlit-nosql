import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = "uber_ny.csv"

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text("Loading data...")
data = load_data(1000)
data_load_state.text("Done! (using cache)")

# Some number in the range 0-23
hour_to_filter = st.slider('Hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


sidebar = st.sidebar
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")