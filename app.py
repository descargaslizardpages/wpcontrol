import streamlit as st
import requests

# 1. Configuración básica
st.set_page_config(page_title="LizardPages Hub")

# 2. Seguridad ultra-simple
if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    st.title("🔒 Acceso")
    clave = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if clave == "1234":
            st.session_state["login"] = True
            st.rerun()
        else:
            st.error("Incorrecta")
    st.stop()

# 3. El Panel (Sin columnas, una cosa debajo de otra para evitar errores)
st.title("🦎 LizardPages Hub")

# Datos de tu sitio
nombre = "LizardPages Principal"
url = "https://lizardpages.com"
usuario = "LP"
pas_wp = "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"

st.write(f"### Gestionando: {nombre}")
st.write(f"URL: {url}")

if st.button("🔌 Probar Conexión"):
    try:
        # Petición simple a la API
        r = requests.get(f"{url}/wp-json/wp/v2/posts", auth=(usuario, pas_wp), timeout=10)
        if r.status_code == 200:
            st.success("✅ ¡CONECTADO! La API responde correctamente.")
        else:
            st.warning(f"⚠️ Error del servidor: {r.status_code}")
    except Exception as e:
        st.error(f"❌ Error de red: {e}")

st.divider()
st.link_button("🚀 Ir al Escritorio de WordPress", f"{url}/wp-admin")
