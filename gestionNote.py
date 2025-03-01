import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestion des Notes", page_icon="logo.png")
st.image("logo.png", width=100)
st.title("Application de Gestion des Notes")
submit = st.form_submit_button("Enregistrer")


if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nom et Prénom", "Module", "Note finale"])

with st.form("form_notes"):
    nom_prenom = st.text_input("Nom et Prénom")
    module = st.text_input("Module")
    note = st.number_input("Note finale", min_value=0.0, max_value=20.0, step=0.1)
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <button type="submit"  padding: 10px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">Enregistrer</button>
        </div>
    """, unsafe_allow_html=True)
    

if submit:
        if nom_prenom and module:
            new_entry = pd.DataFrame({
                "Nom & Prénom": [nom_prenom],
                "Module": [module],
                "Note finale": [note]
            })
            st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
            st.success("Note enregistrée avec succès !")
        else:
            st.error("Veuillez remplir tous les champs!")

st.subheader("Notes enregistrées")
st.dataframe(st.session_state.data)