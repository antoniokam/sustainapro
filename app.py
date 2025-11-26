# main.py
import streamlit as st

st.set_page_config(page_title="SustainaPro 2025", page_icon="leaf", layout="wide")

st.title("SustainaPro 2025 – Bilancio di Sostenibilità ESRS")
st.markdown("### Edizione Enterprise Multiutente – C.M. Service")
st.image("https://img.icons8.com/fluency/100/000000/leaf.png", width=100)

if 'authentication_status' not in st.session_state or not st.session_state["authentication_status"]:
    st.info("Effettua il login dalla pagina laterale →")
else:
    st.success(f"Benvenuto, {st.session_state['name']}!")

    st.write("Usa il menu a sinistra per navigare tra le sezioni.")
