import streamlit as st
import requests

# 1. CONFIGURACIÓN INICIAL (DEBE SER LA PRIMERA LÍNEA DE CÓDIGO)
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")

# 2. SISTEMA DE SEGURIDAD
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🦎 Acceso LizardPages")
    pwd = st.text_input("Introduce la clave maestra:", type="password")
    if st.button("Entrar"):
        if pwd == "1234":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Clave incorrecta")
    st.stop() # Detiene la ejecución aquí si no hay login

# 3. DISEÑO Y MARCA (Solo se ejecuta si el login es correcto)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Exo 2', sans-serif; }
    .stButton>button { 
        background-color: #00a0fe; 
        color: white; 
        border-radius: 10px; 
        border: none;
        font-weight: bold;
    }
    h1 { color: #00a0fe; }
    </style>
    """, unsafe_content_html=True)

st.title("🦎 LizardPages Command Center")

# 4. BASE DE DATOS DE SITIOS
mis_sitios = [
    {
        "nombre": "LizardPages Principal", 
        "url": "https://lizardpages.com", 
        "user": "LP", 
        "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"
    },
]

# 5. PANEL VISUAL
st.subheader("Gestión de Sitios")

for sitio in mis_sitios:
    with st.container():
        col1, col2, col3 = st.columns()
        
        with col1:
            st.write(f"**{sitio['nombre']}**")
            st.caption(sitio['url'])
            
        with col2:
            if st.button(f"🔍 Verificar Salud", key=f"h_{sitio['nombre']}"):
                try:
                    # Probamos conexión con la API de WordPress
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", 
                                     auth=(sitio['user'], sitio['pass']), timeout=10)
                    if res.status_code == 200:
                        st.success("✅ Online")
                    else:
                        st.warning(f"⚠️ Error {res.status_code}")
                except:
                    st.error("❌ Caído")
                    
        with col3:
            st.link_button("🚀 Abrir Admin", f"{sitio['url']}/wp-admin")
        
        st.divider()

# 6. BARRA LATERAL (Sidebar)
with st.sidebar:
    st.header("Herramientas de Red")
    st.write("Bienvenido, Gerling")
    if st.button("Cerrar Sesión"):
        st.session_state["password_correct"] = False
        st.rerun()
