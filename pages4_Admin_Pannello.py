pages/4_Admin_Pannello.py
import streamlit as st
import yaml
import bcrypt
from yaml.loader import SafeLoader
from yaml.dumper import SafeDumper
import os

if st.session_state.get("role") != "admin":
    st.error("Accesso negato. Solo l'amministratore può accedere a questa pagina.")
    st.stop()

st.title("Pannello Amministratore")

def save_config(config):
    with open("../auth/authenticator.yaml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

with st.form("nuovo_utente"):
    st.subheader("Crea nuovo utente")
    nuovo_user = st.text_input("Username (es. giuseppe.verdi)")
    nome = st.text_input("Nome completo")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Crea utente")

    if submitted:
        if not nuovo_user or not password:
            st.error("Compila tutti i campi")
        elif nuovo_user in st.session_state.get("credentials", {}).get("usernames", {}):
            st.error("Utente già esistente")
        else:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode(), salt).decode()
            with open("../auth/authenticator.yaml") as f:
                config = yaml.load(f, Loader=SafeLoader)
            if 'usernames' not in config['credentials']:
                config['credentials']['usernames'] = {}
            config['credentials']['usernames'][nuovo_user] = {
                "email": email,
                "name": nome,
                "password": hashed,
                "role": "user"
            }
            save_config(config)
            st.success(f"Utente {nuovo_user} creato con successo!")
            st.rerun()

st.subheader("Elimina utente")
utenti = list(st.session_state.get("credentials", {}).get("usernames", {}).keys())
utente_da_eliminare = st.selectbox("Seleziona utente da eliminare", [u for u in utenti if u != "admin"])
if st.button("Elimina utente"):
    with open("../auth/authenticator.yaml") as f:
        config = yaml.load(f, Loader=SafeLoader)
    del config['credentials']['usernames'][utente_da_eliminare]
    save_config(config)
    st.success(f"Utente {utente_da_eliminare} eliminato")

    st.rerun()
