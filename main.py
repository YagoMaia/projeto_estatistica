import math
import pandas as pd
from metodos import MetodosMatematicos

dados = [21, 20, 20, 20, 28, 22, 22, 22, 21, 21, 21, 28, 22, 22, 22, 21, 21, 21, 59, 90, 23]

tabela = MetodosMatematicos(dados)

df = pd.DataFrame(tabela.dados_tabela)

print("Programa Finalizado")