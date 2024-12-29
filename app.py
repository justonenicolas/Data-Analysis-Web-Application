import pandas as pd
import streamlit as stl
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

stl.title("# Cree gráficos basados en su selección")
stl.write("En esta página web usted podrá crear gráficos de su selección a partir de la información proveniente del archivo del histórico de ventas de autos en Estados Unidos")

hist_button = stl.button("Crear Histograma", type="primary") # Crear botón que genera el histograma

if hist_button:
    # Escribir el mensaje de salida
    stl.header("Histograma creado")
    
    # Crear el gráfico
    fig = px.histogram(df, x="odometer")
    
    # Mostrar gráfico interactivo en Streamlit
    stl.plotly_chart(fig, use_container_width=True)


scatter_button = stl.button("Crear Gráfico de Dispersión", type="primary") # Crear botón que genera el gráfico de dispersión

if scatter_button:
    # Escribir el mensaje de salida
    stl.header("Gráfico de Dipsersión creado")
    
    # Crear el gráfico
    fig = px.histogram(df, x="odometer", y="condition")
    
    # Mostrar gráfico interactivo en Streamlit
    stl.plotly_chart(fig, use_container_width=True)