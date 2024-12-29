import pandas as pd
import streamlit as stl
import plotly.express as px

df = pd.read_csv("vehicles_us.csv") # Cargar DataFrame

stl.title("Cree gráficos basados en su selección") # Titulo de la página
stl.write("En esta página web usted podrá crear los gráficos de su selección a partir de la información proveniente del archivo del histórico de ventas de autos en Estados Unidos") # Descrpción de página


# Almacenar nombres de columnas y preparar columnas de trabajo
column_names = df.columns
col1, col2 = stl.columns(2)

# Crear listas de opciones para definir los campos a graficar
with col1:
    x_var = stl.radio("Seleccione el **primer** campo (Eje Horizontal)",
                      options=column_names)
    
with col2:
    y_var = stl.radio("Seleccione el **segundo** campo (Eje Vertical)",
                      options=column_names)


hist_button = stl.button("Crear Histograma", type="primary") # Crear botón que genera el histograma

if hist_button:
    # Escribir el mensaje de salida
    stl.header("Histograma creado")
    
    # Crear el gráfico
    fig = px.histogram(df, x=x_var)
    
    # Mostrar gráfico interactivo en Streamlit
    stl.plotly_chart(fig, use_container_width=True)


scatter_button = stl.button("Crear Gráfico de Dispersión", type="primary") # Crear botón que genera el gráfico de dispersión

if scatter_button:
    # Escribir el mensaje de salida
    stl.header("Gráfico de Dipsersión creado")
    
    # Crear el gráfico
    fig = px.histogram(df, x=x_var, y=y_var)
    
    # Mostrar gráfico interactivo en Streamlit
    stl.plotly_chart(fig, use_container_width=True)