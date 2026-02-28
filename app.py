import streamlit as st
import requests

# 1. INICIO OBLIGATORIO
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")

# 2. SEGURIDAD (Clave: 1234)
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        st.title("🦎 Acceso Privado LizardPages")
        pwd = st.text_input("Contraseña Maestra:", type="password")
        if st.button("Entrar"):
            if pwd == "1234":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Acceso denegado")
        return False
    return True

if check_password():
    # 3. ESTILO VISUAL (#00a0fe y Exo 2)
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&display=swap');
        html, body, [class*="css"] { font-family: 'Exo 2', sans-serif; }
        .stButton>button { background-color: #00a0fe; color: white; border-radius: 12px; border: none; font-weight: bold; }
        .status-box { padding: 10px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #00a0fe; }
        </style>
        """, unsafe_content_html=True)

    st.title("🦎 LizardPages Command Center")
    st.write("Panel de control para Hosting Unlimited Pro")

    # 4. TUS SITIOS (Agrega aquí los nuevos clientes)
    mis_sitios = [
        {"nombre": "LizardPages Principal", "url": "https://lizardpages.com", "user": "LP", "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"},
        # Ejemplo de cómo añadir otro:
        # {"nombre": "Cliente Ejemplo", "url": "https://ejemplo.com", "user": "admin", "pass": "XXXX XXXX XXXX"},
    ]

    # 5. RESUMEN DE ESTADO RÁPIDO
    st.subheader("🌐 Estado de la Red de Sitios")
    
    for sitio in mis_sitios:
        with st.container():
            col1, col2, col3, col4 = st.columns()
            
            with col1:
                st.markdown(f"**{sitio['nombre']}**")
                st.caption(sitio['url'])
            
            with col2:
                # Botón de Salud - Ahora con reporte de plugins
                if st.button(f"🔍 Salud", key=f"health_{sitio['nombre']}"):
                    try:
                        r = requests.get(f"{sitio['url']}/wp-json/wp/v2/plugins", auth=(sitio['sitio_user' if 'sitio_user' in sitio else 'user'], sitio['pass']), timeout=10)
                        if r.status_code == 200:
                            st.success(f"Online: {len(r.json())} plugins")
                        else:
                            st.warning(f"Problema (Código {r.status_code})")
                    except:
                        st.error("⚠️ SITIO CAÍDO")

            with col3:
                # Ver entradas rápido
                if st.button(f"📝 Entradas", key=f"posts_{sitio['nombre']}"):
                    r = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", auth=(sitio['user'], sitio['pass']))
                    if r.status_code == 200:
                        st.info(f"{len(r.json())} entradas detectadas")

            with col4:
                st.link_button("🚀 Entrar a WP", f"{sitio['url']}/wp-admin")
            
            st.divider()

    # 6. HERRAMIENTAS MASIVAS (Sidebar)
    with st.sidebar:
        st.image("https://lizardpages.com/wp-content/uploads/2024/01/logo-lizardpages.png", width=150) # Pon tu logo aquí
        st.header("Herramientas")
        if st.button("🔄 Actualizar Todo (Próximamente)"):
            st.write("Esta función requiere un script adicional en cada sitio.")
