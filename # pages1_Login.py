# pages/1_Login.py - VERSIONE DEFINITIVA PER STREAMLIT CLOUD
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import os

# Percorso corretto per Streamlit Cloud (usa root del repo)
config_path = os.path.join(os.getcwd(), "auth", "authenticator.yaml")

if not os.path.exists(config_path):
    st.error("❌ File auth/authenticator.yaml non trovato. Controlla GitHub.")
    st.stop()

with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Accedi a SustainaPro 2025', 'sidebar')

if authentication_status:
    st.sidebar.success(f"✅ Benvenuto, {name}!")
    authenticator.logout('Logout', 'sidebar')
    st.session_state.username = username
    st.session_state.role = config['credentials']['usernames'][username]['role']
    st.session_state.name = name
    st.session_state.authentication_status = True
elif authentication_status == False:
    st.sidebar.error('❌ Username o password errati')
elif authentication_status == None:
    st.sidebar.warning('⚠️ Inserisci le credenziali')
