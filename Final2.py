import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

# Side Bar
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")

#Date Time
titanic_link = 'titanic.csv'

titanic_data = pd.read_csv(titanic_link)

today = datetime.date.today()
today_date = st.date_input('Current date', today)

st.success('Current date %s: ' % str(today_date))

sidebar.header("Dataset")
agree = sidebar.checkbox("show DataSet ? ")
if agree:
    st.dataframe(titanic_data)
    
selected_town = st.radio("Select Emabrk Town",
                         titanic_data['embark_town'].unique())
st.write("Selected Embark Town;", selected_town)

st.write(titanic_data.query(f"""embark_town==@selected_town"""))

st.markdown("___")

optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
                           (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

st.dataframe(subset_fare)

# Graphs
fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Historgrama del Titanic")
st.pyplot(fig)

st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuánto pagaron las clases del Titanic?')

st.header("Gráfico de barras del Titanic")
st.pyplot(fig2)

st.markdown("___")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Gráfico de Dispersión del Titanic")
st.pyplot(fig3)

#San Francisco Map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.title("San Francisco Map")
st.header("Using Streamlit and Mapbox")

st.map(map_data)

# Uber Pickup Map
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
