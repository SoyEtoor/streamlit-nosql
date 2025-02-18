import pandas as pd
import streamlit as st
import datetime

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title('titanic app')
sidebar = st.sidebar

today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)

st.success('Current date %s: ' % str(today_date))

# Display the content of the dataset if checkbox is true

st.header("Dataset")
agree = sidebar.checkbox("show DataSet ? ")
if agree:
    st.dataframe(titanic_data)
    


sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")