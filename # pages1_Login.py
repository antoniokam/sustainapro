# pages/1_Login.py
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import os

config_path = "../auth/authenticator.yaml"
if not os.path.exists(config_path):
    st.error("File di configurazione non trovato. Crea la cartella 'auth' e il file authenticator.yaml")
    st.stop()

with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    "sustainapro_2025",
    "random_key_123456789",
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Accedi a SustainaPro 2025', 'main')

if st.session_state["authentication_status"]:
    st.success(f"Accesso effettuato come **{name}**")
    role = config['credentials']['usernames'][username]['role']
    st.session_state.role = role
    st.session_state.username = username
    st.rerun()
elif st.session_state["authentication_status"] is False:
    st.error("Username o password errati")
elif st.session_state["authentication_status"] is None:
    st.warning("Inserisci le credenziali")