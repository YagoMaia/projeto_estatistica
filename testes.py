import streamlit as st
import plotly.express as px
import pandas as pd
from metodos import MetodosMatematicos
from random import randint
import os

dados = []

for b in range(0, 100):
    dados.append(randint(20, 30))

tabela = MetodosMatematicos(dados)

df = pd.DataFrame(tabela.dados_tabela)

print(tabela.li)