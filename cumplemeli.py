import streamlit as st

st.title("Feliz Cumpleaños 🎂")

nombre = st.text_input("Ingresa el nombre:")

if st.button("Mostrar mensaje"):
    mensaje = f"""
¡Feliz cumpleaños, {nombre}!

Espero que hayas tenido un día maravilloso
lleno de alegría y momentos especiales.

Perdón por no decírtelo antes,
pero te deseo éxitos Meli siendo sincero.
te quiero mucho
"""
    st.success(mensaje)
