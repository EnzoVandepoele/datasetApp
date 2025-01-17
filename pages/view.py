﻿import streamlit as st
import pandas as pd
import numpy as np
from inspect import signature
import pandas as pd
import datetime

st.markdown(
    """
    <style>
    body {
        background-image: url("https://www.numerama.com/wp-content/uploads/2016/09/grumpycat.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialiser session_state si nécessaire
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
if "new_row" not in st.session_state:
    st.session_state.new_row = {}
if "col_names" not in st.session_state:
    st.session_state.col_names = []
if "show_download_buttons" not in st.session_state:
    st.session_state.show_download_buttons = False
if "show_signature_button" not in st.session_state:
    st.session_state.show_signature_button = False
    
    # Demander le nom de la nouvelle colonne
col_name = st.text_input("Entrez le nom de la colonne à afficher")
if col_name:  # Vérifier si le nom de la colonne n'est pas vide
   if col_name:
    # Vérifier si la colonne existe dans le DataFrame
    if col_name in st.session_state.df.columns:
        st.write(f"Valeurs de la colonne {col_name} :")
        
        # Afficher les valeurs de la colonne
        st.dataframe(st.session_state.df[[col_name]])
        
        # Ajouter des critères de sélection supplémentaires
        if st.session_state.df[col_name].dtype == 'int64' or st.session_state.df[col_name].dtype == 'float64':
            # Si la colonne est numérique, permettre à l'utilisateur de définir une plage de valeurs
            min_val = st.number_input(f"Valeur minimum pour {col_name}", value=float(st.session_state.df[col_name].min()))
            max_val = st.number_input(f"Valeur maximum pour {col_name}", value=float(st.session_state.df[col_name].max()))
            filtered_df = st.session_state.df[(st.session_state.df[col_name] >= min_val) & (st.session_state.df[col_name] <= max_val)]
        else:
            # Si la colonne est textuelle, permettre à l'utilisateur de rechercher une correspondance partielle
            search_term = st.text_input(f"Termes à rechercher dans {col_name}")
            filtered_df = st.session_state.df[st.session_state.df[col_name].str.contains(search_term, case=False, na=False)]
        
        # Afficher le DataFrame filtré
        st.write(f"Données filtrées selon les critères pour {col_name} :")
        st.dataframe(filtered_df)
    else:
        st.write(f"La colonne '{col_name}' n'existe pas dans le DataFrame.")