import math
import pandas as pd

dados = [21, 20, 20, 20, 28, 22, 22, 22, 21, 21, 21]
tamanho_amostra = len(dados)
posicao_max = tamanho_amostra - 1
media = sum(dados) / len(dados)
print(media)
sorted(dados)
print(posicao_max)
print(tamanho_amostra)
# print(int(tamanho_amostra / 2))
print(int(9 / 2))
mediana = (
    (dados[int(tamanho_amostra / 2)] + dados[int(tamanho_amostra / 2) + 1]) / 2
    if tamanho_amostra % 2 == 0
    else dados[int((tamanho_amostra - 1) / 2)]
)
print(mediana)
amplitude_max = max(dados) - min(dados)

print(amplitude_max)

soma_variancia = 0
for v in dados:
    soma_variancia += (media - v) ** 2

variancia = soma_variancia / tamanho_amostra

print(variancia)

k =  math.ceil(math.sqrt(24))

c = (max(dados) - min(dados))/k-1

limite_inferior = min(dados) - c/2

print(limite_inferior)

lista_intervalos_ini = []
lista_intervalos_fim = [] # Fazer divisão de classes com todos os dados

futuro_df = {}
for b in range(0, k):
    lista_intervalos_ini.append(limite_inferior + c*b)
    lista_intervalos_fim.append(limite_inferior + c*(b+1))

for e in range(0, k):
    futuro_df['Intervalos'] = f"{lista_intervalos_ini[e]} --| {lista_intervalos_fim[e]}"

# print(intervalos)

# for key,val in intervalos.items():
#     print(f"{key} ---| {val}")
#     print("="*20)

for e in futuro_df:
    print(e)