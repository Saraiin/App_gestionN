import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestion des Notes", page_icon="logo.png")
st.image("logo.png", width=100)
st.title("Application de Gestion des Notes")
st.markdown("""
    <p style="color: grey; font-size: 16px;">Veuillez remplir le formulaire ci-dessous pour enregistrer une note.</p>
""", unsafe_allow_html=True)


if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nom et Prénom", "Module", "Note finale"])

with st.form("form_notes"):
    nom_prenom = st.text_input("Nom et Prénom")
    module = st.text_input("Module")
    note = st.number_input("Note finale", min_value=0.0, max_value=20.0, step=0.1)
    submit = st.form_submit_button("Enregistrer")
    

if submit:
        if nom_prenom and module:
            new_entry = pd.DataFrame({
                "Nom et Prénom": [nom_prenom],
                "Module": [module],
                "Note finale": [note]
            })
            st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
            st.success("Note enregistrée avec succès !")
        else:
            st.error("Veuillez remplir tous les champs!")

st.subheader("Notes enregistrées")
st.dataframe(st.session_state.data)