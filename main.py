import streamlit as st
import datetime

st.set_page_config(
    page_title="Supervision Fresadoras",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# Programa de supervisión Fresadoas. Estamos de pruebas",
    },
)

respuesta = st.radio("Pregunta", ["Casa", "Trabajo", "Viaje"])
st.write(f"Has elegido {respuesta}")
