import streamlit as st


def delete(conexion):
    st.title("🗑️ Borrar videojuegos")
    # Obtenemos la lista con los juegos gracias a este metodo.
    todos_los_juegos = list(conexion.find())
    nombres_juegos = [juego["Nombre"] for juego in todos_los_juegos]

    #El usuario va elegir el juego que quiere borrar
    if nombres_juegos:
        juegos_a_borrar = st.selectbox("Selecciona el juego que quieres borrar:", nombres_juegos)
        
        #Boton de confirmación que quiere borrar
        if st.button("Eliminar"):
            resultado = conexion.delete_one({"Nombre": juegos_a_borrar})

            if resultado.deleted_count > 0:
                st.warning(f"Se ha eliminado '{juegos_a_borrar}' de la base de datos.")
                st.rerun()
    else:
        st.write("No hay juegos para eliminar.") 