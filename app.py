import streamlit as st

# 1. Configuración de Marca
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎")

# Estilo rápido (Azul #00a0fe)
st.markdown("""
    <style>
    .stButton>button { background-color: #00a0fe; color: white; border-radius: 10px; width: 100%; font-weight: bold; }
    h1 { color: #00a0fe; }
    </style>
    """, unsafe_content_html=True)

if "lista" not in st.session_state:
    st.session_state["lista"] = []

st.title("🦎 LizardPages Hub")
st.write("Gestiona tus accesos rápidos a WordPress.")

# 2. Formulario para el Alumno
with st.form("agregar", clear_on_submit=True):
    nombre = st.text_input("Nombre del Sitio (ej: Mi Tienda)")
    link_magico = st.text_input("Pega aquí tu Enlace Mágico de WordPress:")
    if st.form_submit_button("➕ Guardar Sitio"):
        if nombre and link_magico:
            st.session_state["lista"].append({"n": nombre, "l": link_magico})
            st.rerun()

st.divider()

# 3. Botones de Acceso
if not st.session_state["lista"]:
    st.info("Aún no tienes sitios. Agrega uno arriba para probar.")
else:
    for i, sitio in enumerate(st.session_state["lista"]):
        col1, col2 = st.columns()
        with col1:
            # ¡ESTE ES EL BOTÓN QUE HACE LA MAGIA!
            st.link_button(f"🚀 ENTRAR A {sitio['n'].upper()}", sitio['l'])
        with col2:
            if st.button("Eliminar", key=f"del_{i}"):
                st.session_state["lista"].pop(i)
                st.rerun()
