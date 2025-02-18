import pandas as pd
import numpy as np
import streamlit as st

sidebar = st.sidebar
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# Create the title for the web app
st.title("San Francisco Map")
st.header("Using Streamlit and Mapbox")

st.map(map_data)
