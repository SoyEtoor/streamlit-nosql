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

# Side Bar
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")
