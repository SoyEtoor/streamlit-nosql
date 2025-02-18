import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

#Tittle and sidebar
sidebar = st.sidebar
sidebar.title('Titanic Data')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")

#Checkbox to show the dataset overview
agree = sidebar.checkbox('Show dataset Overview')
if agree:
    st.dataframe(titanic_data)


#Histograma 
fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header('Histograma - Fare ')
st.pyplot(fig)  # streamlit function to display matplotlib plots