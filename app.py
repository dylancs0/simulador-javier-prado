import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulador Tráfico Av. Javier Prado",
    layout="wide"
)

st.title("Simulador de Tráfico Adaptativo (IA)")

# Lectura del archivo HTML local
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Incrustación del componente HTML en la app
components.html(html_data, height=900, scrolling=True)