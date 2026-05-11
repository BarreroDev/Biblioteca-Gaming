import streamlit as st


def form(conexion):
    st.title("📝 Añadir nuevo juego")
    
    # Metemos el formulario AQUÍ DENTRO
    with st.form("nuevo_juego_form", clear_on_submit=True):
        nombre = st.text_input("Nombre del Videojuego")
        img = st.text_input("URL del juego")
        plataforma = st.selectbox("Plataformas: ", ["PC", "Xbox", "PS5", "Nintendo", "Android", "iOs", "Wii"])
        nota = st.slider("Tu puntuación: ", 0, 10, 5)
        volver = st.selectbox("¿Volverás a jugar?:", ["Sí", "No", "Quizás"])
        opinion = st.text_area("Tu opinión:")
        boton_guardar = st.form_submit_button("Guardar")

        if boton_guardar:
            if nombre:
                documento = {
                    "Nombre": nombre, 
                    "Imagen": img,
                    "Plataforma": plataforma, 
                    "Rejugar": volver, 
                    "Nota": nota, 
                    "Opinion": opinion
                }
                conexion.insert_one(documento)
                st.success(f"¡{nombre} guardado!")
                # st.rerun() # Opcional: para que al ir a Biblioteca ya salga
            else:
                st.error("Escribe el nombre.")