import streamlit as st
import requests

# 1. Configuración obligatoria
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

# 3. Encabezado con tu marca
st.title("🦎 LizardPages Command Center")
st.write(f"Bienvenido de nuevo, Gerling.")

# 4. Base de datos de tus sitios (Aquí agregas tus clientes)
mis_sitios = [
    {
        "nombre": "LizardPages Principal", 
        "url": "https://lizardpages.com", 
        "user": "LP", 
        "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"
    },
]

st.subheader("Gestión de Sitios")

# 5. Listado de sitios corregido
for sitio in mis_sitios:
    with st.container():
        # Corregido: Ahora indicamos que queremos 3 columnas
        col1, col2, col3 = st.columns()
        
        with col1:
            st.write(f"**{sitio['nombre']}**")
            st.caption(sitio['url'])
            
        with col2:
            if st.button(f"Verificar Salud", key=f"btn_{sitio['nombre']}"):
                try:
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", 
                                     auth=(sitio['user'], sitio['pass']), timeout=10)
                    if res.status_code == 200:
                        st.success("Conectado")
                    else:
                        st.warning(f"Error {res.status_code}")
                except:
                    st.error("No responde")
                    
        with col3:
            # Botón estilizado para ir al admin
            st.link_button("Ir al Admin 🚀", f"{sitio['url']}/wp-admin")
        
        st.divider()

# 6. Barra lateral
with st.sidebar:
    st.info("Panel de Control v1.0")
    if st.button("Cerrar Sesión"):
        st.session_state["authenticated"] = False
        st.rerun()
