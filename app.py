import streamlit as st
import requests

# Configuración visual con tu marca LizardPages
st.set_page_config(page_title="LizardPages Hub", page_icon="🦎", layout="wide")

# Estilo personalizado (Color #00a0fe)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; color: white; }}
    .stButton>button {{ background-color: #00a0fe; color: white; border-radius: 8px; }}
    .stHeader {{ font-family: 'Exo 2', sans-serif; }}
    </style>
    """, unsafe_content_html=True)

st.title("🦎 LizardPages Multi-Site Manager")
st.write("Gestiona tus sitios y los de tus clientes desde un solo lugar.")

# Tu base de datos de sitios
mis_sitios = [
    {"nombre": "LizardPages", "url": "https://lizardpages.com", "user": "LP", "pass": "ZYk2 2z3H vSL2 A0D8 Hr3u ibG6"},
    # Añade aquí más clientes siguiendo el mismo formato
]

# Interfaz de Gestión
for sitio in mis_sitios:
    with st.expander(f"🌐 {sitio['nombre']} - {sitio['url']}"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"Revisar Plugins", key=f"plugins_{sitio['nombre']}"):
                try:
                    res = requests.get(f"{sitio['url']}/wp-json/wp/v2/plugins", auth=(sitio['user'], sitio['pass']))
                    if res.status_code == 200:
                        plugins = res.json()
                        updates = [p for p in plugins if p.get('update')]
                        st.info(f"Total: {len(plugins)} | ⚠️ Pendientes: {len(updates)}")
                    else:
                        st.error("Error de conexión")
                except:
                    st.error("Sitio no alcanzable")

        with col2:
            if st.button(f"Ver Entradas", key=f"posts_{sitio['nombre']}"):
                res = requests.get(f"{sitio['url']}/wp-json/wp/v2/posts", auth=(sitio['user'], sitio['pass']))
                if res.status_code == 200:
                    st.success(f"Entradas publicadas: {len(res.json())}")

        with col3:
            st.link_button("Abrir WP-Admin", f"{sitio['url']}/wp-admin")
