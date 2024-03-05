import streamlit as st
import pandas as pd
from metodos import MetodosMatematicos
import altair as alt

dados = [10,20,30,51,51,51,51,51, 10, 12, 15, 17, 20, 21, 25]

tabela = MetodosMatematicos(dados)

df = pd.DataFrame(tabela.dados_tabela)

#st.title("Tabela com os dados")
st.markdown("<h1 style='text-align: center'>Tabela com os dados</h1>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

dados_bar = tabela.dados_tabela

del dados_bar['fac'], dados_bar['fr']
dados_bar['fi'].pop(-1)
dados_bar['Intervalos'] = tabela.li

df_bar = pd.DataFrame(dados_bar)

bar = alt.Chart(df_bar).mark_bar(size=20).encode(y = alt.Y("fi", title = "Frequências"), x = "Intervalos")

st.altair_chart(bar, use_container_width=True)