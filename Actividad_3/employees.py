import streamlit as st
import pandas as pd

# Cargar datos con caché
@st.cache_data
def load_data(nrows=500):
    df = pd.read_csv("employees.csv")
    return df.head(nrows)

df = load_data()

# Título y descripción
title = "Employee Data Dashboard"
description = "Aplicación interactiva para analizar datos de empleados"

st.title(title)
st.write(description)

# Sidebar con checkbox para mostrar/ocultar dataframe
st.sidebar.header("Opciones")
show_data = st.sidebar.checkbox("Mostrar Dataframe Completo")
if show_data:
    st.write(df)

# Buscador de empleados
st.sidebar.subheader("Buscar Empleado")
search_id = st.sidebar.text_input("Employee_ID")
search_hometown = st.sidebar.text_input("Hometown")
search_unit = st.sidebar.text_input("Unit")

filtered_df = df.copy()
if search_id:
    filtered_df = filtered_df[filtered_df["Employee_ID"].str.contains(search_id, case=False)]
if search_hometown:
    filtered_df = filtered_df[filtered_df["Hometown"].str.contains(search_hometown, case=False)]
if search_unit:
    filtered_df = filtered_df[filtered_df["Unit"].str.contains(search_unit, case=False)]

st.write("### Resultados de la búsqueda")
st.write(filtered_df)

# Alumno
sidebar = st.sidebar
sidebar.title('This is the sidebar')
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")