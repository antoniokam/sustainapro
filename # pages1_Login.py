# pages/1_Login.py  ← VERSIONE GARANTITA Streamlit Cloud 2025
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import os

# Percorso corretto su Streamlit Cloud
config_path = os.path.join(os.path.dirname(__file__), "..", "auth", "authenticator.yaml")

with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config.get('cookie', {}).get('name', 'sustainapro_cookie'),
    config.get('cookie', {}).get('key', 'random_key_2025'),
    config.get('cookie', {}).get('expiry_days', 30)
)

name, authentication_status, username = authenticator.login('Accedi', 'sidebar')

if authentication_status:
    st.sidebar.success(f"Benvenuto, {name}!")
    authenticator.logout('Logout', 'sidebar')
    st.session_state.username = username
    st.session_state.role = config['credentials']['usernames'][username].get('role', 'user')
elif authentication_status == False:
    st.sidebar.error('Username/password errati')
elif authentication_status == None:
    st.sidebar.warning('Inserisci le credenziali')
