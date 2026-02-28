import streamlit as st
import requests

# 1. ESTO DEBE IR PRIMERO SIEMPRE
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")

# 2. SISTEMA DE SEGURIDAD
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.title("🦎 Acceso LizardPages")
        pwd = st.text_input("Introduce la clave maestra:", type="password")
        if st.button("Entrar"):
            if pwd == "1234": # Tu contraseña
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Clave incorrecta")
        return False
    return True

if check_password():
    # 3. DISEÑO CON TU MARCA (#00a0fe y Exo 2)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&display=swap');
        html, body, [class*="css"] { font-family: 'Exo 2', sans-serif; }
        .stButton>button { background-color: #00a0fe; color: white; border-radius: 10px; border: none; }
        h1 { color: #00a0fe; }
        </style>
        """, unsafe_content_html=True)

    st.title("🦎 LizardPages Command Center")

    # 4. TUS SITIOS
    mis_sitios = [
        {"nombre": "LizardPages", "url": "https://lizardpages.com", "user": "LP", "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"},
    ]

    # 5. PUBLICADOR MASIVO (Sidebar)
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

    # 6. LISTADO VISUAL
    st.subheader("Estado de la Red")
    for sitio in mis_sitios:
        with st.container():
            col1, col2, col3 = st.columns()
            with col1:
                st.write(f"**{sitio['nombre']}**")
                st.caption(sitio['url'])
            with col2:
                if st.button(f"Plugins", key=f"btn_{sitio['nombre']}"):
                    try:
                        res = requests.get(f"{sitio['url']}/wp-json/wp/v2/plugins", auth=(sitio['user'], sitio['pass']))
                        if res.status_code == 200:
                            st.info(f"{len(res.json())} Plugins")
                    except:
                        st.error("Error")
            with col3:
                st.link_button("Abrir Admin", f"{sitio['url']}/wp-admin")
            st.divider()
