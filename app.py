import streamlit as st
import requests

# 1. Configuración de Marca LizardPages
st.set_page_config(page_title="LizardPages Hub - Alumnos", page_icon="🦎")

# 2. Seguridad de Acceso (Tu clave de taller)
if "acceso_alumno" not in st.session_state:
    st.session_state["acceso_alumno"] = False

if not st.session_state["acceso_alumno"]:
    st.title("🦎 Taller LizardPages")
    st.write("Bienvenido al panel de gestión para alumnos.")
    clave = st.text_input("Introduce la clave del taller:", type="password")
    if st.button("Entrar al Panel"):
        if clave == "1234": # Esta es la clave que les darás a ellos
            st.session_state["acceso_alumno"] = True
            st.rerun()
        else:
            st.error("Clave incorrecta. Solicítala en el grupo de alumnos.")
    st.stop()

# 3. Interfaz para el Alumno
st.title("🦎 Mi Gestor WordPress")
st.info("Introduce los datos de tu sitio para verificar el estado.")

# Formulario de entrada de datos
with st.form("credenciales_alumno"):
    col1, col2 = st.columns(2)
    with col1:
        url_alumno = st.text_input("URL de tu sitio (con https://)", placeholder="https://tusitio.com")
        user_alumno = st.text_input("Tu Usuario de WordPress")
    with col2:
        pass_alumno = st.text_input("Contraseña de Aplicación (24 caracteres)", type="password")
        st.caption("Genérala en tu WordPress: Usuarios > Perfil > Contraseñas de aplicación")
    
    boton_conectar = st.form_submit_button("🚀 Verificar mi Sitio")

# 4. Lógica de conexión
if boton_conectar:
    if not url_alumno or not user_alumno or not pass_alumno:
        st.warning("Por favor, completa todos los campos.")
    else:
        try:
            # Limpiamos la URL por si el alumno pone una barra al final
            url_limpia = url_alumno.rstrip('/')
            endpoint = f"{url_limpia}/wp-json/wp/v2/posts"
            
            with st.spinner("Conectando con tu servidor..."):
                r = requests.get(endpoint, auth=(user_alumno, pass_alumno), timeout=15)
            
            if r.status_code == 200:
                st.success(f"✅ ¡Conexión exitosa con {url_alumno}!")
                st.balloons()
                
                # Pequeño reporte para el alumno
                posts = r.json()
                st.write(f"📊 **Resumen rápido:**")
                st.write(f"- Tienes {len(posts)} entradas publicadas recientemente.")
            else:
                st.error(f"❌ Error {r.status_code}: Revisa que el usuario y la contraseña de aplicación sean correctos.")
        
        except Exception as e:
            st.error(f"❌ No pudimos encontrar tu sitio. Asegúrate de escribir bien la URL.")

# 5. Barra lateral con recursos
with st.sidebar:
    st.header("Recursos para Alumnos")
    st.link_button("Hosting Unlimited Pro", "https://lizardpages.com")
    if st.button("Cerrar Sesión"):
        st.session_state["acceso_alumno"] = False
        st.rerun()
