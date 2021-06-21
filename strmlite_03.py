# Copyright (c) 2021 Jordi Gual
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

DATA_SOURCE = '/home/jordi/Documents/Datasets/Iris/iris.csv'

def load_data():
    # Carreguem nrows instàncies
    data = pd.read_csv(DATA_SOURCE, names=['Sepal_l', 'Sepal_w', 'Petal_l', 'Petal_w', 'Class'])
    return data

###
# Main Program
###

st.title('Iris Again')
data_load_state = st.text('Loading data...')
data = load_data()
data
data_load_state.text('Loading data...done!')

# Anem a establir alguns filtres
st.subheader('Choose filters')
# Filtre de classe
class_options = list(set(data['Class'])) # Totes les classes diferents
class_filter = st.multiselect('Class', class_options, default=['Iris-setosa'])
# Dos sliders per a seleccionar el rang de longitud de sèpal
sepal_l_filter = st.slider('Sepal_length', 4.0, 8.0, (4.0, 8.0), step=0.1)
# sepal_l_top = st.slider('Upper Sepal_length', 4.0, 8.0, (4.0, 8.0), step=0.1)

chosen = data[data['Sepal_l'].between(sepal_l_filter[0],sepal_l_filter[1])]
chosen = chosen[chosen['Class'].isin(class_filter)]
chosen

# Algunes estadístiques:
med = chosen['Sepal_l'].median()
avg = chosen['Sepal_l'].mean()
mn = chosen['Sepal_l'].min()
mx = chosen['Sepal_l'].max()
st.markdown(f'Sepal Lengths: Avg. {avg:.1f} | Med. {med:.1f} | Min. {mn:.1f} | Max {mx:.1f}')