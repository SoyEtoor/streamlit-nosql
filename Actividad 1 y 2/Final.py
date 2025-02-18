import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

# First App
st.title('hello streamlit')
st.header('welcome streamlit')

# Read Names
names_link = 'dataset.csv'

names_data = pd.read_csv(names_link)
st.title('names dataset')
st.dataframe(names_data)

# Search By Names
DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

def search_matches(name, df):
    if name:
        return df[df['name'].str.contains(name, case=False, na=False)]

st.title("Search Names in Dataset")

df = load_data()

myname = st.text_input("Enter a name:")

if myname:
    results = search_matches(myname, df)
    st.write(f"### Found {len(results)} matches:")
    st.dataframe(results)
else:
    st.info("Please enter a name to search.")
    
# Search By Range
DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df = df.reset_index()  
    return df

def search_by_index(index, df):
    if index.isdigit():  
        index = int(index)
        if index in df.index:
            return df.loc[[index]]
    return pd.DataFrame() 

def search_by_range(start, end, df):
    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
        return df.iloc[start:end+1]  
    return pd.DataFrame()

df = load_data()

st.title("Search in Database")

st.subheader("Search by Index")
index_search = st.text_input("Enter an index:")
if st.button("Search Name by Index"):
    result = search_by_index(index_search, df)
    if not result.empty:
        st.write("### Match Found:")
        st.dataframe(result)
    else:
        st.warning("No match found for this index.")

st.subheader("Search by Range of Indexes")
start_index = st.text_input("Start Index:")
end_index = st.text_input("End Index:")

if st.button("Search Names in Range"):
    range_results = search_by_range(start_index, end_index, df)
    if not range_results.empty:
        st.write(f"### Found {len(range_results)} matches:")
        st.dataframe(range_results)
    else:
        st.warning("No matches found in this range.")
        
# Search By Sex
DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

def filter_by_sex(sex, df):
    return df[df["sex"] == sex]

df = load_data()

st.title("Filter by Gender")

selected_sex = st.selectbox("Select Gender:", ["F", "M"])

if st.button("Filter"):
    filtered_df = filter_by_sex(selected_sex, df)
    count = len(filtered_df)

    st.write(f"### Found {count} {'women' if selected_sex == 'F' else 'men'} in the dataset.")
    st.dataframe(filtered_df)
    
# Cache
DATA_URL = "dataset.csv"
LENGTH_DATA = sum(1 for _ in open(DATA_URL)) - 1 

@st.cache_data
def load_data(nrows):
    return pd.read_csv(DATA_URL, nrows=nrows)

st.title("Cache Example")

nrows = st.number_input("Number of rows to load", 1, LENGTH_DATA)

df = load_data(nrows)

st.dataframe(df)

#Activida 2

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
