# pages/1_Login.py - VERSIONE SEMPLICE (senza YAML, 100% funzionante)
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.sidebar.title("🔐 Login SustainaPro 2025")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Accedi"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.session_state.username = "admin"
            st.session_state.role = "admin"
            st.session_state.name = "Amministratore"
            st.sidebar.success("✅ Login riuscito!")
            st.rerun()
        elif username == "antonio.canonico" and password == "Antcan2025":
            st.session_state.logged_in = True
            st.session_state.username = "antonio.canonico"
            st.session_state.role = "user"
            st.session_state.name = "Antonio Canonico"
            st.sidebar.success("✅ Login riuscito!")
            st.rerun()
        else:
            st.sidebar.error("❌ Credenziali errate")
    st.stop()

st.sidebar.success(f"Benvenuto, {st.session_state.name}!")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()
