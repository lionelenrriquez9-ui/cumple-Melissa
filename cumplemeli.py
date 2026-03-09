import streamlit as st

st.title("Feliz Cumpleaños 🎂")

nombre = st.text_input("Ingresa el nombre:")

if st.button("Mostrar mensaje"):
    mensaje = f"""
¡Feliz cumpleaños {nombre}!

Bueno mali perdon por decirte feliz cumple muy tarde, perdon enserio y bueno espero que estes bien en lima y
que te vallan bien siempre en los estudios, cuando hagas tu empresa me contratas aunque sea de limpia baños jsjajs
y si diosito quiere nos veremos o si tu deseas tmb, nd mas que decir cuidate meli y otra vez lo digo FELIZ CUMPLEAÑOSS.
Espero que hayas tenido un día maravilloso
lleno de alegría y momentos especiales.

perdon perdon perdon por no decírtelo antes,
espero que me perdones 🥺🥺 
Te quiero mucho 
"""
    st.success(mensaje)
    
    # Mostrar globos
    st.balloons()


