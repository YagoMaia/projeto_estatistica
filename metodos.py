import math

class MetodosMatematicos():
    
    def __init__(self, dados):
        self.dados = dados
        self.tamanho_amostra = len(self.dados)
        self.media = self.calcular_media()
        self.media = self.calcular_media()
        self.mediana = self.calcular_mediana()
        self.amplitude = self.calcular_amplitude()
        self.k = self.calcular_k()
        self.c = self.calcular_c()
        self.variancia = self.calcular_variancia()
        self.limite_inferior = self.calcular_limite_inferior()
        self.dados_tabela = self.montar_tabela()
            
    def calcular_media(self):
        media = sum(self.dados)/self.tamanho_amostra
        return media
    
    def calcular_mediana(self):
        mediana = (self.dados[int(self.tamanho_amostra / 2)] + self.dados[int(self.tamanho_amostra / 2) + 1]) / 2 if self.tamanho_amostra % 2 == 0 else self.dados[int((self.tamanho_amostra - 1) / 2)]
        return mediana
    
    def calcular_amplitude(self):
        amplitude = max(self.dados) - min(self.dados)
        return amplitude
        
    def calcular_k(self):
        k = round(math.sqrt(self.tamanho_amostra))
        return k
    
    def calcular_c(self):
        c = self.amplitude / (self.k - 1)
        return c
    
    def calcular_variancia(self):
        soma = 0
        for valor in self.dados:
            soma += (self.media - valor) ** 2
        variancia = soma/self.tamanho_amostra
        return variancia
    
    def calcular_limite_inferior(self):
        limite_inferior = min(self.dados) - self.c/2
        return limite_inferior
    
    def montar_listas_intervalos(self):
        lista_intervalos_ini = []
        lista_intervalos_fim = []
        
        for b in range(0, self.k):
            lista_intervalos_ini.append(self.limite_inferior + self.c*b)
            lista_intervalos_fim.append(self.limite_inferior + self.c*(b+1))
        
        return lista_intervalos_ini, lista_intervalos_fim
    
    def printar_classes(self):
        for key, value in self.dados_tabela.items():
            print(key, value)
            
    def montar_tabela(self):
        fi = []
        fr = []
        fac = []
        li, lf = self.montar_listas_intervalos()
        intervalos = []
        for c in range(0, self.k):
            cont_fi = 0
            for valor in self.dados:
                if li[c] <= valor < lf[c]:
                    cont_fi += 1
            fi.append(cont_fi)
            fr.append(round(cont_fi/self.tamanho_amostra, 3))
            intervalos.append(f"{li[c]} --| {lf[c]}")
            if c == 0:
                fac.append(fr[0])
            else:
                fac.append(round(fac[c-1] + fr[c], 3))
        
        intervalos.append("Total")
        fi.append(sum(fi))
        fr.append(sum(fr))
        fac.append("-")
        
        return {'Intervalos': intervalos, 'fi' : fi, 'fr' : fr, 'fac' : fac}