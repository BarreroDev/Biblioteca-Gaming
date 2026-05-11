import streamlit as st
import pandas as pd

def library(conexion):
    st.title("🎮 Biblioteca Gaming")
    st.write("---")
    st.header("📚 Juegos en tu Biblioteca")
    
    # Metemos la lógica de la tabla AQUÍ DENTRO
    datos_mongo = list(conexion.find())
    if datos_mongo:
       for juego in datos_mongo:# todo ira dentro de un for para que recorra los datos.
           
           with st.container(border=True):
               # En este caso se divide en dos columnas una para la imgen y otra para los datos.
               col_img, col_info = st.columns([1,3])

               with col_img:
                    
                   if "Imagen" in juego and isinstance(juego["Imagen"], str) and juego["Imagen"].startswith("http"):
                       st.image(juego["Imagen"], use_container_width=True)
                   else:
                       st.image("https://via.placeholder.com/150?text=Sin+Portada", use_container_width=True)   

               with col_info:
                     st.subheader(juego["Nombre"])
                     st.write(f"**Plataforma:** {juego['Plataforma']}")
                     st.write(f"**Nota:** {juego['Nota']}/10")
                     st.info(f"💬 {juego.get('Opinion', 'Sin opinión')}")        

    else:
        st.info("La biblioteca esta vacía.")
