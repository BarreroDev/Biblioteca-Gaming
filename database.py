import os
from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit as st

# Cargamos las variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

@st.cache_resource
def obtener_conexion():
    """Establece la conexión con la colección de MongoDB."""
    try:
        cliente = MongoClient(MONGO_URI)
        db = cliente[MONGO_DB_NAME]
        return db[MONGO_COLLECTION]
    except Exception as e:
        st.error(f"Error al conectar a MongoDB: {e}")
        return None