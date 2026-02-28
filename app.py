import streamlit as st
import requests

# 1. Configuración obligatoria (Debe ser la primera línea)
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")

# 2. Seguridad (Clave: 1234)
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

# 3. Diseño y Estilo LizardPages (#00a0fe y Exo 2)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Exo 2', sans-serif; }
    .stButton>button { 
        background-color: #00a0fe; 
        color: white; 
        border-radius: 10px; 
        border: none;
        width: 100%;
    }
    h1, h2, h3 { color: #00a0fe; font-family: 'Exo 2', sans-serif; }
    </style>
    """, unsafe_content_html=True)

st.title("🦎 LizardPages Command Center")
st.write(f"Bienvenido de nuevo, Gerling.")

# 4. Base de datos de sitios (Añade aquí tus clientes de Hosting Unlimited Pro)
mis_sitios = [
    {
        "nombre": "LizardPages Principal", 
        "url": "https://lizardpages.com", 
        "user": "LP", 
        "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"
    },
]

st.subheader("Gestión de Sitios")

# 5. Listado de sitios (Corregido el error de columnas)
for sitio in mis_sitios:
    with st.container():
        # Aquí definimos el ancho de las 3 columnas [Nombre, Salud, Enlace]
        col1, col2, col3 = st.columns()
        
        with col1:
            st.write(f"**{sitio['nombre']}**")
            st.caption(sitio['url'])
            
        with col2:
            if st.button(f"🔍 Salud", key=f"check_{sitio['nombre']}"):
                try:
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", 
                                     auth=(sitio['user'], sitio['pass']), timeout=10)
                    if res.status_code == 200:
                        st.success("Online")
                    else:
                        st.warning(f"Error {res.status_code}")
                except Exception:
                    st.error("Caído")
                    
        with col3:
            st.link_button("Ir al Admin 🚀", f"{sitio['url']}/wp-admin")
        
        st.divider()

# 6. Barra lateral
with st.sidebar:
    st.image("https://lizardpages.com/wp-content/uploads/2024/01/logo-lizardpages.png", width=120)
    st.info("Panel v1.0 - Hosting Unlimited Pro")
    if st.button("Cerrar Sesión"):
        st.session_state["authenticated"] = False
        st.rerun()
