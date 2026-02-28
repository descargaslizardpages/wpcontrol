import streamlit as st
import requests

# 1. Configuración de página (Siempre primero)
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎")

# 2. Sistema de Seguridad Simple
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🦎 Acceso LizardPages")
    clave = st.text_input("Introduce la clave maestra:", type="password")
    if st.button("Entrar"):
        if clave == "1234":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Clave incorrecta")
    st.stop()

# 3. Contenido de la App (Solo se ve si estás autenticado)
st.title("🦎 LizardPages Command Center")
st.write(f"Bienvenido de nuevo, Gerling.")

# Base de datos de tus sitios
mis_sitios = [
    {
        "nombre": "LizardPages Principal", 
        "url": "https://lizardpages.com", 
        "user": "LP", 
        "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"
    },
]

st.subheader("Gestión de Sitios")

for sitio in mis_sitios:
    with st.container():
        col1, col2, col3 = st.columns()
        
        with col1:
            st.write(f"**{sitio['nombre']}**")
            st.caption(sitio['url'])
            
        with col2:
            if st.button(f"Verificar", key=f"btn_{sitio['nombre']}"):
                try:
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", 
                                     auth=(sitio['user'], sitio['pass']), timeout=10)
                    if res.status_code == 200:
                        st.success("Online")
                    else:
                        st.warning(f"Error {res.status_code}")
                except:
                    st.error("Caído")
                    
        with col3:
            st.link_button("Ir al Admin", f"{sitio['url']}/wp-admin")
        
        st.divider()

# Barra lateral simple
with st.sidebar:
    if st.button("Cerrar Sesión"):
        st.session_state["authenticated"] = False
        st.rerun()
