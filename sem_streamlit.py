#import streamlit as st
#import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
from metodos import MetodosMatematicos
from random import randint
#import os

#dados = [10, 20, 30, 51, 51, 51, 51, 51, 10, 12, 15, 17, 20, 21, 25]
dados = []

#planilha = pd.read_excel(f"{os.getcwd()}/planilha.xlsx")
#dados_planilha = planilha['nome coluna']

# st.set_page_config(layout="wide")

for b in range(0, 100):
    dados.append(randint(20, 30))

tabela = MetodosMatematicos(dados)

df = pd.DataFrame(tabela.dados_tabela)

#st.markdown("<h1 style='text-align: center'>Tabela com os dados</h1>", unsafe_allow_html=True)
#st.dataframe(df, use_container_width=True)

dados_bar = tabela.dados_tabela

#print(tabela.novos_dados)

del dados_bar["fac"], dados_bar["fr"]
dados_bar["fi"].pop(-1)
dados_bar["Intervalos"].pop(-1)

df_bar = pd.DataFrame(dados_bar)

fig, ax = plt.subplots(1,1)

ax.hist(tabela.novos_dados)

#ax.plot(1, 1, 'ro')

plt.show()