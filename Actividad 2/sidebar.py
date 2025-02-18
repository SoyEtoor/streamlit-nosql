# Importamos la librería de Streamlit
import streamlit as st

# Crear el título para la aplicación web
st.title("Mi Primera App con Streamlit")

# Creamos el sidebar
sidebar = st.sidebar

# Agregamos un título y texto al sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")

#Agregamos headers a la sección principal
st.write("""
         Este es un simple ejemplo de una app para predecir
         ¡Esta app predice mis datos!
         """)
