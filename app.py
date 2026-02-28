import streamlit as st
import pandas as pd

# 1. Configuración de Marca LizardPages
st.set_page_config(page_title="LizardPages Hub - Acceso Rápido", page_icon="🦎")

# Estilo para que los botones se vean bien
st.markdown("""
    <style>
    .stButton>button { background-color: #00a0fe; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    h3 { color: #00a0fe; }
    </style>
    """, unsafe_content_html=True)

if "mis_sitios" not in st.session_state:
    st.session_state["mis_sitios"] = []

st.title("🦎 LizardPages Hub")
st.write("Sube tu lista de sitios y accede a todos tus WordPress sin contraseña.")

# 2. SECCIÓN DE CARGA (CSV)
with st.expander("📁 Subir mi lista de sitios (CSV)"):
    archivo = st.file_uploader("Selecciona tu archivo .csv", type=["csv"])
    if archivo:
        try:
            df = pd.read_csv(archivo)
            # Limpiamos y cargamos los datos
            for _, row in df.iterrows():
                # Evitamos duplicados básicos
                if not any(s['url'] == str(row['url']).rstrip('/') for s in st.session_state["mis_sitios"]):
                    st.session_state["mis_sitios"].append({
                        "nombre": row['nombre'],
                        "url": str(row['url']).rstrip('/'),
                        "user": row['user'],
                        "token": row['token']
                    })
            st.success("✅ ¡Lista cargada correctamente!")
        except Exception as e:
            st.error(f"Error: Asegúrate que el CSV tenga las columnas: nombre, url, user, token")

st.divider()

# 3. EL PANEL DE CONTROL (Aquí es donde aparecen los botones)
st.subheader(f"Mis Accesos Directos ({len(st.session_state['mis_sitios'])})")

if not st.session_state["mis_sitios"]:
    st.info("Aún no hay sitios cargados. Sube un CSV o agrega uno manualmente.")
else:
    for i, sitio in enumerate(st.session_state["mis_sitios"]):
        # Usamos una caja para cada sitio
        with st.container():
            col1, col2 = st.columns()
            
            with col1:
                st.markdown(f"### {sitio['nombre']}")
                st.caption(f"📍 {sitio['url']}")
            
            with col2:
                # --- AQUÍ ESTÁ EL BOTÓN DE ENTRADA A WP ---
                # Creamos la URL mágica: sitio.com/?lizard_login=usuario&key=token
                enlace_wp = f"{sitio['url']}/?lizard_login={sitio['user']}&key={sitio['token']}"
                st.link_button(f"🚀 ENTRAR A WP", enlace_wp)
                
                # Botón pequeño para borrar de la lista actual
                if st.button("Eliminar de la lista", key=f"del_{i}"):
                    st.session_state["mis_sitios"].pop(i)
                    st.rerun()
            st.divider()

# 4. BOTÓN MANUAL (Por si no tienen CSV)
with st.sidebar:
    st.header("➕ Agregar Manual")
    with st.form("manual"):
        m_nom = st.text_input("Nombre")
        m_url = st.text_input("URL")
        m_usr = st.text_input("Usuario")
        m_tok = st.text_input("Token", type="password")
        if st.form_submit_button("Añadir Sitio"):
            st.session_state["mis_sitios"].append({"nombre":m_nom, "url":m_url.rstrip('/'), "user":m_usr, "token":m_tok})
            st.rerun()
    
    if st.button("🗑️ Limpiar todo el panel"):
        st.session_state["mis_sitios"] = []
        st.rerun()
