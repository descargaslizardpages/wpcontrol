import streamlit as st
import requests

# 1. CONFIGURACIÓN DE SEGURIDAD
def check_password():
    """Retorna True si el usuario introdujo la contraseña correcta."""
    def password_entered():
        if st.session_state["password"] == "TU_CONTRASEÑA_AQUÍ": # <--- CAMBIA ESTO
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Contraseña de Acceso", type="password", on_change=password_entered, key="password")
        st.write("🔒 Área restringida para administración de sitios.")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Contraseña de Acceso", type="password", on_change=password_entered, key="password")
        st.error("😕 Contraseña incorrecta")
        return False
    else:
        return True

# 2. DISEÑO Y MARCA
if check_password():
    st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")
    
    # Aplicamos tu color de marca #00a0fe y tipografía Exo 2
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&display=swap');
        html, body, [class*="css"] { font-family: 'Exo 2', sans-serif; }
        .stButton>button { background-color: #00a0fe; color: white; border-radius: 20px; width: 100%; }
        </style>
        """, unsafe_content_html=True)

    st.title("🦎 LizardPages Multi-Site Manager")
    
    # Base de datos de tus sitios (Añade aquí los que necesites)
    mis_sitios = [
        {"nombre": "LizardPages", "url": "https://lizardpages.com", "user": "LP", "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"},
    ]

    # Panel de control
    for sitio in mis_sitios:
        with st.container():
            col1, col2, col3 = st.columns()
            with col1:
                st.subheader(sitio['nombre'])
                st.write(sitio['url'])
            with col2:
                if st.button(f"Verificar Salud", key=f"check_{sitio['nombre']}"):
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/plugins", auth=(sitio['user'], sitio['pass']))
                    if res.status_code == 200:
                        st.success(f"Online - {len(res.json())} Plugins")
            with col3:
                st.link_button("Abrir Admin", f"{sitio['url']}/wp-admin")
            st.divider()
