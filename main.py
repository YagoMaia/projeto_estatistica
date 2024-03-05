import streamlit as st
import pandas as pd
from metodos import MetodosMatematicos
import altair as alt

dados = [21, 20, 20, 20, 28, 22, 22, 22, 21, 21, 21, 42, 23, 47, 53, 13, 19, 22, 17, 20, 20, 34, 34, 34]

tabela = MetodosMatematicos(dados)

df = pd.DataFrame(tabela.dados_tabela)

#st.title("Tabela com os dados")
st.markdown("<h1 style='text-align: center'>Tabela com os dados</h1>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

dados_bar = tabela.dados_tabela

del dados_bar['fac'], dados_bar['fr']
dados_bar['fi'].pop(-1)
dados_bar['Intervalos'].pop(-1)

df_bar = pd.DataFrame(dados_bar)

bar = alt.Chart(df_bar).mark_bar().encode(y = "fi", x = "Intervalos").configure_axisX(labelAngle=0)

st.altair_chart(bar, use_container_width=True)