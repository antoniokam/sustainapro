# pages/3_Generatore_Bilancio.py
import streamlit as st

if not st.session_state.get("authentication_status"):
    st.stop()

st.title("Generatore Bilancio di Sostenibilità")
st.write("Qui genereremo automaticamente il Bilancio di Sostenibilità in Word e PDF")
st.info("In arrivo nella prossima versione (48h)")