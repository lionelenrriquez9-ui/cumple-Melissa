import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Cumpleaños 🎂", page_icon="🎉")

st.title("Nombre de la cumpleañera(empieza con M)")
st.write("Tengo un pequeño mensaje para ti 💌")

nombre = st.text_input("Ingresa el nombre:")

if st.button("Abrir sorpresa"):
    
    if nombre.strip() == "":
        st.warning("Pon el nombre de melissa")
    else:
        
        # Animación de carga
        with st.spinner("Preparando sorpresa..."):
            time.sleep(2)

        st.balloons()
        st.snow()

        st.success(f"""
🎉¡Feliz cumpleaños, {nombre}! 

Bueno meli perdon por decirte feliz cumple muy tarde, perdon enserio y bueno espero que estes bien en lima y
que te vallan bien siempre en los estudios, cuando hagas tu empresa me contratas aunque sea de limpia baños jsjajs
y si diosito quiere nos veremos o si tu deseas tmb, nd mas que decir cuidate meli y otra vez lo digo FELIZ CUMPLEAÑOSS.
Espero que hayas tenido un día maravilloso
lleno de alegría y momentos especiales.

perdon perdon perdon por no decírtelo antes,
espero que me perdones 🥺🥺 
con mucho cariño  
Te quiero mucho.
""")

        st.subheader("🎂 Un pequeño pastel para ti")
        st.write("espero volvamos a vernoss")





