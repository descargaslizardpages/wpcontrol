import streamlit as st

# 1. Configuración básica (Blindada)
st.set_page_config(page_title="LizardPages Hub")

# 2. Base de Datos temporal (Ilimitada)
if "mis_sitios" not in st.session_state:
    st.session_state["mis_sitios"] = []

st.title("🦎 LizardPages Hub")
st.write("Agrega tus sitios para entrar sin contraseña.")

# 3. Formulario Simple (Sin columnas para evitar errores)
with st.form("nuevo_sitio", clear_on_submit=True):
    nombre = st.text_input("Nombre del Proyecto:")
    url = st.text_input("URL (https://...):")
    usuario = st.text_input("Usuario Administrador:")
    token = st.text_input("Palabra Secreta (Token):", type="password")
    
    if st.form_submit_button("➕ Guardar en mi Lista"):
        if nombre and url and usuario and token:
            st.session_state["mis_sitios"].append({
                "nombre": nombre, "url": url.rstrip('/'), 
                "user": usuario, "key": token
            })
            st.rerun()

st.divider()

# 4. Listado de Sitios (Uno debajo del otro, sin columnas complejas)
st.subheader(f"Mis WordPress ({len(st.session_state['mis_sitios'])})")

for i, sitio in enumerate(st.session_state["mis_sitios"]):
    st.write(f"### 🌐 {sitio['nombre']}")
    st.caption(f"URL: {sitio['url']}")
    
    # Enlace Mágico
    enlace = f"{sitio['url']}/?lizard_login={sitio['user']}&key={sitio['key']}"
    st.link_button(f"🚀 ENTRAR A {sitio['nombre'].upper()}", enlace)
    
    if st.button("Eliminar Sitio", key=f"del_{i}"):
        st.session_state["mis_sitios"].pop(i)
        st.rerun()
    st.divider()
