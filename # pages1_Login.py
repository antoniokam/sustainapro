# pages/1_Login.py - VERSIONE FUNZIONANTE SU STREAMLIT CLOUD
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import os

# Percorso corretto su Streamlit Cloud
config_path = os.path.join(os.path.dirname(__file__), "../auth/authenticator.yaml")

if not os.path.exists(config_path):
    st.error("File di configurazione non trovato. Contatta l'amministratore.")
    st.stop()

with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config.get('cookie', {}).get('name', 'sustainapro_cookie'),
    config.get('cookie', {}).get('key', 'random_key'),
    config.get('cookie', {}).get('expiry_days', 30)
)

name, authentication_status, username = authenticator.login('Accedi a SustainaPro 2025', 'sidebar')

if authentication_status:
    st.sidebar.success(f"Benvenuto, {name}!")
    authenticator.logout('Logout', 'sidebar')
    st.session_state['name'] = name
    st.session_state['authentication_status'] = True
    st.session_state['username'] = username
    st.session_state['role'] = config['credentials']['usernames'][username].get('role', 'user')
elif authentication_status is False:
    st.sidebar.error('Username o password errati')
elif authentication_status is None:
    st.sidebar.warning('Inserisci le credenziali')
