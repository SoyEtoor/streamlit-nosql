import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Cardiovascular Disease Dataset", layout="wide")

# Logo del proyecto y título
st.image("cardio.png", width=100)
st.title("Cardiovascular Disease Dataset")

# Descripción de las columnas
st.subheader("Descripción de los datos")
description = {
    "age": "Edad en días",
    "gender": "Género (1: Mujer, 2: Hombre)",
    "height": "Altura en cm",
    "weight": "Peso en kg",
    "ap_hi": "Presión arterial sistólica",
    "ap_lo": "Presión arterial diastólica",
    "cholesterol": "Colesterol (1: Normal, 2: Alto, 3: Muy alto)",
    "gluc": "Glucosa (1: Normal, 2: Alto, 3: Muy alto)",
    "smoke": "Fuma (0: No, 1: Sí)",
    "alco": "Consumo de alcohol (0: No, 1: Sí)",
    "active": "Actividad física (0: No, 1: Sí)",
    "cardio": "Enfermedad cardiovascular (0: No, 1: Sí)"
}

st.write(pd.DataFrame(list(description.items()), columns=["Columna", "Descripción"]))

# Cargar datos
DATA_URL = "cardio_train.csv"
LENGTH_DATA = sum(1 for _ in open(DATA_URL)) - 1 

@st.cache_data
def load_data(nrows):
    return pd.read_csv(DATA_URL, nrows=nrows)

st.title("Cache")

nrows = st.number_input("Número de filas a cargar", 1, LENGTH_DATA)
df = load_data(nrows)

# Mostrar datos completos
st.dataframe(df)

# Buscador de información en el dataset
st.sidebar.header("Buscador de Información")
search_term = st.sidebar.text_input("Buscar en el dataset")
if st.sidebar.button("Buscar"):
    results = df[df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)]
    st.write(results)

# Filtrado de información
st.sidebar.header("Filtros")
category_options = st.sidebar.selectbox("Selecciona una categoría (opcional):", ["Mostrar todas"] + list(df.columns))
gender_options = st.sidebar.multiselect("Selecciona género:", df["gender"].unique())
cholesterol_options = st.sidebar.multiselect("Selecciona nivel de colesterol:", df["cholesterol"].unique())
glucose_options = st.sidebar.multiselect("Selecciona nivel de glucosa:", df["gluc"].unique())

filtered_df = df.copy()
if gender_options:
    filtered_df = filtered_df[filtered_df["gender"].isin(gender_options)]
if cholesterol_options:
    filtered_df = filtered_df[filtered_df["cholesterol"].isin(cholesterol_options)]
if glucose_options:
    filtered_df = filtered_df[filtered_df["gluc"].isin(glucose_options)]

# Mostrar datos según selección
st.write("Datos filtrados:")
if category_options == "Mostrar todas":
    st.dataframe(filtered_df.head(10))
else:
    st.dataframe(filtered_df[[category_options]].head(10))

# Histograma de edades
st.header("Distribución de edades")
plt.figure(figsize=(10, 5))
sns.histplot(df["age"] / 365, bins=30, kde=True)
plt.xlabel("Edad (años)")
st.pyplot(plt)
st.write("Este histograma muestra la distribución de edades en el dataset.")

# Gráfica de barras: Cholesterol vs. Cardiovascular Disease
st.header("Relación entre Colesterol y Enfermedad Cardiovascular")
cholesterol_counts = df.groupby("cholesterol")["cardio"].sum()
plt.figure(figsize=(8, 5))
cholesterol_counts.plot(kind="bar", color=["blue", "orange", "red"])
plt.xlabel("Nivel de Colesterol")
plt.ylabel("Casos de Enfermedad Cardiovascular")
st.pyplot(plt)
st.write("Esta gráfica muestra cuántas personas con diferentes niveles de colesterol tienen enfermedad cardiovascular.")

# Gráfica de dispersión: Peso vs. Presión Sanguínea
st.header("Relación entre Peso y Presión Sanguínea")
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df["weight"], y=df["ap_hi"], alpha=0.5)
plt.xlabel("Peso (kg)")
plt.ylabel("Presión Arterial Sistólica (ap_hi)")
st.pyplot(plt)
st.write("Este gráfico muestra la relación entre el peso y la presión sanguínea sistólica.")

# Alumno
st.sidebar.title('Alumno')
st.sidebar.write('Héctor Miguel Torres Martínez')
st.sidebar.write('zs22004346')
st.sidebar.image("yogris.jpeg")
