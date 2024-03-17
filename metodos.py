import math

class MetodosMatematicos():
    
    def __init__(self, dados):
        """
        Iniciando a classe
        """
        self.dados = dados
        self.novos_dados = []
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
        self.li, self.lf = self.montar_listas_intervalos()
            
    def calcular_media(self):
        """
        Método Responsável por calcular a média
        """
        media = sum(self.dados)/self.tamanho_amostra
        return media
    
    def calcular_mediana(self):
        """
        Método Responsável por calcular a mediana
        """
        mediana = (self.dados[int(self.tamanho_amostra / 2)] + self.dados[int(self.tamanho_amostra / 2) + 1]) / 2 if self.tamanho_amostra % 2 == 0 else self.dados[int((self.tamanho_amostra - 1) / 2)]
        return mediana
    
    def calcular_amplitude(self):
        """
        Método responsável por calcular a amplitude
        """
        amplitude = max(self.dados) - min(self.dados)
        return amplitude
        
    def calcular_k(self):
        """
        Método responsável por calcular o k
        """
        k = round(math.sqrt(self.tamanho_amostra))
        return k
    
    def calcular_c(self):
        """
        Método responsável por calcular o c
        """
        c = round(self.amplitude / (self.k - 1), 2)
        return c
    
    def calcular_variancia(self):
        """
        Método responsável por calcular a Variância
        """
        soma = 0
        for valor in self.dados:
            soma += (self.media - valor) ** 2
        variancia = soma/self.tamanho_amostra
        return variancia
    
    def calcular_limite_inferior(self):
        """
        Método responsável por calcular o limite inferior
        """
        limite_inferior = min(self.dados) - self.c/2
        return limite_inferior
    
    def montar_listas_intervalos(self):
        """
        Método responsável por calcular os intervalos
        """
        lista_intervalos_ini = []
        lista_intervalos_fim = []
        
        for b in range(0, self.k):
            lista_intervalos_ini.append(round(self.limite_inferior + self.c*b, 3))
            lista_intervalos_fim.append(round(self.limite_inferior + self.c*(b+1), 3))
        
        return lista_intervalos_ini, lista_intervalos_fim
    
    def printar_classes(self):
        """
        Método responsável por printar as classes baseado nos dados
        """
        for key, value in self.dados_tabela.items():
            print(key, value)
            
    def montar_tabela(self):
        """
        Método responsável por criar a tabela
        """
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
                    self.novos_dados.append(li[c])
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
        fac.append(None)
        
        return {'Intervalos': intervalos, 'fi' : fi, 'fr' : fr, 'fac' : fac}