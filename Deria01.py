import numpy as np
import pandas as pd
import streamlit as st

# Titol de l'aplicació
st.title('DERIA: Data Enhancement, Review, Insights & Analysis')

# Subtitol Tasques
st.sidebar.subheader('Tasques a fer:')

# Tria múltiple de tasques
tsks = ['Entrada de dades',
        'EDA',
        'Pre-tractament',
        'Classificació',
        'Regressió',
        'No supervisat']
tsks_selection = st.sidebar.multiselect('', tsks, default=['Entrada de dades'])

# Entrada de dades
if 'Entrada de dades' in tsks_selection:
    # Lectura del fitxer de dades
    