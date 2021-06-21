# Copyright (c) 2021 Jordi Gual
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import streamlit as st

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

if __name__ == '__main__':

    # Titol de la WebPage
    st.title('Deria: Classificador automàtic')

    # Escriure unes dades
    st.write("Here's our first attempt at using data to create a table:")
    df = pd.DataFrame({'first column': [1, 2, 3, 4],
                       'second column': [5, 6, 7, 8]})
    df # Si es posa la variable sola, és com fer un write
    
    # Activació/desactivació d'una gràfica
    if st.checkbox('Activar gràfica?'):
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
    
    # Visualització d'un mapa
    map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                            columns=['lat', 'lon'])
    st.map(map_data)

    # Selecció d'opcions
    #option = st.selectbox('Which number do you like best?', df['first column'])
    #'You selected: ', option

    # Sidebar
    # Selecció d'opcions
    option = st.sidebar.selectbox('Which number do you like best?', df['first column'])
    'You selected:', option

    # Markdown
    st.sidebar.markdown("""### Kernel functions

The kernel function can be any of the following:

* linear: $\langle x, x'\\rangle$
* polynomial: $(\gamma \langle x, x'\\rangle + r)^d$, where $d$ is specified by parameter *degree*, $r$ by *coef0*.
* rbf: $\exp(-\gamma \|x-x'\|^2)$, where $\gamma$ is specified by parameter *gamma*, must be greater than 0. **By default!**
* sigmoid: $\\tanh(\gamma \langle x,x'\\rangle + r)$ , where $r$ is specified by *coef0*.
""")