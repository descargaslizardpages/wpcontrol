import streamlit as st
import requests
import hashlib

# 1. Configuración
st.set_page_config(page_title="LizardPages Hub - AutoLogin", page_icon="🦎")

if "sitios" not in st.session_state:
    st.session_state["sitios"] = []

st.title("🦎 LizardPages: Acceso Rápido")
st.write("Agrega tus sitios para entrar sin contraseña.")

# 2. Formulario para agregar sitios
with st.expander("➕ Agregar nuevo sitio"):
    with st.form("nuevo_sitio"):
        nombre = st.text_input("Nombre del sitio (ej. Mi Blog)")
        url = st.text_input("URL (https://...)")
        user = st.text_input("Usuario admin")
        token = st.text_input("Token de Seguridad (Inventa una palabra secreta)", type="password")
        if st.form_submit_button("Guardar Sitio"):
            st.session_state["sitios"].append({"nombre": nombre, "url": url.rstrip('/'), "user": user, "token": token})
            st.rerun()

# 3. Listado de Sitios con Auto-Login
st.subheader("Mis WordPress")

for i, sitio in enumerate(st.session_state["sitios"]):
    col1, col2, col3 = st.columns()
    
    with col1:
        st.write(f"**{sitio['nombre']}**")
    
    with col2:
        # Generamos el enlace mágico
        # Enviamos el usuario y el token como validación
        magic_url = f"{sitio['url']}/?lizard_login={sitio['user']}&key={sitio['token']}"
        st.link_button("🚀 Entrar sin Clave", magic_url)
    
    with col3:
        if st.button("Eliminar", key=f"del_{i}"):
            st.session_state["sitios"].pop(i)
            st.rerun()
