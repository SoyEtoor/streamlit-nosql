import pandas as pd
import streamlit as st

names_link = 'dataset.csv'

names_data = pd.read_csv(names_link)
st.title('names dataset')

st.write('Héctor Miguel Torres Martínez')
st.write('zs22004346')
st.image("yogris.jpeg")

st.dataframe(names_data)