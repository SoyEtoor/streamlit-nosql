import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Name App
st.title('Cicles Riding in NY')

# Read Data
nybike = pd.read_csv('citibike-tripdata-2019-01.csv')

# Renombrar Columnas
nybike.rename(columns={'start_lat': 'lat', 'start_lng': 'lon'}, inplace=True)

# Side Bar
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")

# Extraer Hora
nybike['started_at'] = pd.to_datetime(nybike['started_at'])
nybike['hour'] = nybike['started_at'].dt.hour

# Checkbox
sidebar.header("Dataset")
agree = sidebar.checkbox("¿Mostrar Raw Data?")
if agree:
    # Show Raw Data
    st.title('Raw Data')
    st.dataframe(nybike)
    st.markdown("___")

# Slider para seleccionar la hora
sidebar.header("Filtrar por Hora")
selected_hour = sidebar.slider("Selecciona la hora del día:", 0, 23, 12)  # Default: 12 PM
filtered_data = nybike[nybike['hour'] == selected_hour]

# Checkbox
sidebar.header("Recorridos por Hora")
agree = sidebar.checkbox("¿Mostrar Recorridos por Hora?")
if agree:
    # Gráfica de recorridos por hora
    st.title('Número de Recorridos por Hora')
    fig, ax = plt.subplots()
    nybike['hour'].value_counts().sort_index().plot(kind='bar', ax=ax)
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Número de recorridos")
    ax.set_title("Número de recorridos por hora")
    st.pyplot(fig)
    st.markdown("___")
    # Mapa de Recorridos Iniciados
    st.header("Mapa de Recorridos Iniciados a las " + str(selected_hour) + " Horas del Día")
    st.map(filtered_data[['lat', 'lon']])
    st.markdown("___")
    
# Alumno
sidebar.title('Alumno')
sidebar.write('Héctor Miguel Torres Martínez')
sidebar.write('zs22004346')
sidebar.image("yogris.jpeg")
