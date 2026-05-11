import streamlit as st
import pandas as pd
from database import obtener_conexion # <--- Importamos nuestra "herramienta"
from modulos.formulario import form
from modulos.biblioteca import library
from modulos.borrado import delete


# Llamamos a la conexión desde el archivo externo
conexion = obtener_conexion()

# 3. NAVEGACIÓN (EL DIRECTOR)
st.sidebar.title("Navegación:")
pagina = st.sidebar.selectbox("Selecciona una página", ["📚 Biblioteca", "📝 Formulario alta", "🗑️ Borrar juego"])

if pagina == "📚 Biblioteca":
    library(conexion)
elif pagina == "📝 Formulario alta":
    form(conexion)
elif pagina == "🗑️ Borrar juego":
    delete(conexion)