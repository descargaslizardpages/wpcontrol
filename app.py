import streamlit as st
import pandas as pd

# 1. Configuración
st.set_page_config(page_title="LizardPages Hub - Carga Masiva", page_icon="🦎")

if "mis_sitios" not in st.session_state:
    st.session_state["mis_sitios"] = []

st.title("🦎 LizardPages Hub: Gestor Pro")

# 2. SECCIÓN PARA SUBIR CSV
st.subheader("📁 Carga masiva de sitios")
archivo_subido = st.file_uploader("Sube tu archivo CSV (Columnas: nombre, url, user, token)", type=["csv"])

if archivo_subido is not None:
    try:
        df = pd.read_csv(archivo_subido)
        # Convertimos el CSV en la lista que usa la App
        for index, row in df.iterrows():
            st.session_state["mis_sitios"].append({
                "nombre": row['nombre'],
                "url": str(row['url']).rstrip('/'),
                "user": row['user'],
                "key": row['token']
            })
        st.success("✅ ¡Sitios cargados desde el archivo!")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}. Revisa que las columnas sean: nombre, url, user, token")

st.divider()

# 3. LISTADO DE SITIOS
st.subheader(f"Mis WordPress ({len(st.session_state['mis_sitios'])})")

for i, sitio in enumerate(st.session_state["mis_sitios"]):
    # Diseño simple y resistente
    st.markdown(f"### 🌐 {sitio['nombre']}")
    st.write(f"URL: {sitio['url']} | Usuario: {sitio['user']}")
    
    # Enlace Mágico de LizardPages
    enlace = f"{sitio['url']}/?lizard_login={sitio['user']}&key={sitio['key']}"
    
    st.link_button(f"🚀 ENTRAR A {sitio['nombre'].upper()}", enlace)
    
    if st.button(f"Eliminar {sitio['nombre']}", key=f"del_{i}"):
        st.session_state["mis_sitios"].pop(i)
        st.rerun()
    st.divider()

# 4. BOTÓN PARA LIMPIAR TODO
if st.sidebar.button("🗑️ Borrar toda la lista"):
    st.session_state["mis_sitios"] = []
    st.rerun()
