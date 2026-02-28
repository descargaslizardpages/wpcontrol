import streamlit as st
import requests

# 1. Configuración mínima
st.set_page_config(page_title="LizardPages Hub")

# 2. Entrada de datos del alumno
st.title("🦎 LizardPages: Acceso Rápido")
st.write("Configura tu acceso directo a WordPress")

with st.form("config_sitio"):
    url = st.text_input("URL de tu sitio:", placeholder="https://tusitio.com")
    usuario = st.text_input("Tu Usuario admin:")
    # Esta es la palabra clave que el alumno debe poner en su WordPress
    clave_secreta = st.text_input("Tu Palabra Secreta (Token):", type="password")
    
    boton_guardar = st.form_submit_button("Guardar Configuración")

if url and usuario and clave_secreta:
    st.divider()
    st.subheader(f"Panel para: {url}")
    
    # ENLACE MÁGICO: Este es el truco para el Login Automático
    # Enviamos al alumno a su sitio con una "llave" especial
    enlace_magico = f"{url.rstrip('/')}/?lizard_login={usuario}&key={clave_secreta}"
    
    st.write("Haz clic abajo para entrar sin contraseña:")
    st.link_button("🚀 ENTRAR A MI WORDPRESS", enlace_magico)
    
    st.info("Nota: Para que el botón funcione, debes haber pegado el código Snippet en tu WordPress.")
