import streamlit as st

# 1. Configuración de Marca LizardPages
st.set_page_config(page_title="LizardPages Hub - Mis Sitios", page_icon="🦎", layout="wide")

# Estilo visual básico para tus botones
st.markdown("""
    <style>
    .stButton>button { background-color: #00a0fe; color: white; border-radius: 8px; border: none; }
    h1 { color: #00a0fe; }
    </style>
    """, unsafe_content_html=True)

# 2. Inicializar la "Base de Datos" temporal
if "lista_sitios" not in st.session_state:
    st.session_state["lista_sitios"] = []

st.title("🦎 LizardPages: Gestor de Sitios Ilimitados")
st.write("Agrega tus WordPress aquí para entrar con un solo clic.")

# 3. Formulario para agregar sitios (Ilimitados)
with st.expander("➕ Agregar nuevo sitio a mi lista"):
    with st.form("nuevo_sitio", clear_on_submit=True):
        nombre = st.text_input("Nombre del Proyecto (ej: Tienda de Juan)")
        url = st.text_input("URL del sitio (https://...)")
        usuario = st.text_input("Usuario Administrador")
        token = st.text_input("Palabra Secreta (Token)", type="password")
        
        if st.form_submit_button("Guardar en mi Panel"):
            if nombre and url and usuario and token:
                nuevo_item = {
                    "nombre": nombre,
                    "url": url.rstrip('/'),
                    "user": usuario,
                    "key": token
                }
                st.session_state["lista_sitios"].append(nuevo_item)
                st.success(f"✅ {nombre} agregado con éxito.")
                st.rerun()
            else:
                st.warning("Por favor, completa todos los campos.")

# 4. Visualización de la Lista de Sitios
st.subheader(f"Mis Accesos Directos ({len(st.session_state['lista_sitios'])})")

if not st.session_state["lista_sitios"]:
    st.info("Aún no tienes sitios guardados. Usa el botón '+' de arriba.")
else:
    for i, sitio in enumerate(st.session_state["lista_sitios"]):
        # Usamos contenedores para que no fallen las columnas
        with st.container():
            # Creamos una fila visual con 3 partes
            c1, c2, c3 = st.columns()
            
            with c1:
                st.markdown(f"**{sitio['nombre']}**")
                st.caption(sitio['url'])
            
            with c2:
                # Enlace Mágico para el Login Automático
                enlace = f"{sitio['url']}/?lizard_login={sitio['user']}&key={sitio['key']}"
                st.link_button("🚀 Acceder sin Clave", enlace)
            
            with c3:
                if st.button("🗑️", key=f"del_{i}"):
                    st.session_state["lista_sitios"].pop(i)
                    st.rerun()
            st.divider()

# 5. Instrucción para el Alumno
with st.sidebar:
    st.header("⚙️ Configuración")
    st.write("Recuerda que para que el acceso funcione, debes tener instalado el Snippet de LizardPages en cada sitio.")
    if st.button("Limpiar todo el Panel"):
        st.session_state["lista_sitios"] = []
        st.rerun()
