# Copyright (c) 2021 Jordi Gual
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import streamlit as st

# Titol de la pàgina
st.title('Uber dataset prova')

# URL on es troben les dades
data_url = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    # Carreguem nrows instàncies
    data = pd.read_csv(data_url, nrows=nrows)
    # Passem a minúscula el nom de les columnes
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # Passem les tires de 'date/time' a tipus datetime
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

###
# Main Program
###

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 1000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

# Visualitzem les dades llegides, si activem un checkbox
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Visualitzem un histograma
# Nombre de viatges per hora
hist_values = np.histogram(data['date/time'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Visualitzem un mapa amb totes les recollides
st.subheader('Map of all pickups')
st.map(data)

# Visualitzem un mapa amb les recollides d'una hora escollida amb slider

hour_to_filter = st.slider('hour', 0, 23, 17) # Min, max, default
filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# Existeix la funció pydeck_chart, amb moltes més opcions
st.map(filtered_data)