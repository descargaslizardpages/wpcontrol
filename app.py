import streamlit as st
import requests

# 1. SEGURIDAD
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.title("🦎 Acceso LizardPages")
        pwd = st.text_input("Introduce la clave maestra:", type="password")
        if st.button("Entrar"):
            if pwd == "1234": # Tu contraseña actual
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Clave incorrecta")
        return False
    return True

if check_password():
    # 2. CONFIGURACIÓN VISUAL (Tu marca #00a0fe)
    st.set_page_config(page_title="LizardPages Hub", page_icon="🦎")
    st.markdown("""
        <style>
        .stButton>button { background-color: #00a0fe; color: white; border-radius: 10px; }
        h1 { color: #00a0fe; font-family: 'Exo 2'; }
        </style>
        """, unsafe_content_html=True)

    st.title("🦎 LizardPages Command Center")

    # 3. BASE DE DATOS DE CLIENTES
    # Aquí puedes seguir agregando más diccionarios para cada cliente
    mis_sitios = [
        {"nombre": "LizardPages", "url": "https://lizardpages.com", "user": "LP", "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"},
        # {"nombre": "Cliente X", "url": "https://clientex.com", "user": "admin", "pass": "xxxx xxxx xxxx"}
    ]

    # 4. ACCIÓN MASIVA: PUBLICADOR
    with st.sidebar:
        st.header("📢 Anuncio Global")
        titulo_aviso = st.text_input("Título del aviso")
        contenido_aviso = st.text_area("Contenido")
        if st.button("🚀 Publicar en TODOS los sitios"):
            for sitio in mis_sitios:
                data = {'title': titulo_aviso, 'content': contenido_aviso, 'status': 'publish'}
                r = requests.post(f"{sitio['url']}/wp-json/wp/v2/posts", auth=(sitio['user'], sitio['pass']), json=data)
                if r.status_code == 201:
                    st.toast(f"Publicado en {sitio['nombre']}")

    # 5. LISTADO DE SITIOS
    st.subheader("Estado de la Red")
    for sitio in mis_sitios:
        col1, col2, col4 = st.columns()
        with col1:
            st.write(f"**{sitio['nombre']}**")
            st.caption(sitio['url'])
        with col2:
            if st.button("Check Plugins", key=sitio['nombre']):
                res = requests.get(f"{sitio['url']}/wp-json/wp/v2/plugins", auth=(sitio['user'], sitio['pass']))
                if res.status_code == 200:
                    st.info(f"{len(res.json())} Plugins")
        with col4:
            st.link_button("Ir al Admin", f"{sitio['url']}/wp-admin")
        st.divider()
