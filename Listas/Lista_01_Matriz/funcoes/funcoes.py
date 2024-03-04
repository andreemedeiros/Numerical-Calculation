# Funções:
# a) Erro Médio Absoluto;
# b) Erro Médio Quadrático;
# c) Erro Médio Quadrático Normalizado;
# d) Média;
# e) Variância;
# f) Covariância;
# g) oeficiente de Correlação.

# Importa bibliotecas
import numpy as np

from menu.interface import interface

# ----------------- a) Erro Médio Absoluto: ----------------- #
def ema(f, g):
    
    # Diferença absoluta entre as matrizes
    diferenca_absoluta = np.abs(f - g)
    
    # Soma das diferenças absolutas
    soma_diferencas = np.sum(diferenca_absoluta)
    
    # Número total de elementos na matriz
    total_elementos = f.size
    
    # EMA
    ema = soma_diferencas / total_elementos
    
    return ema
# ----------------------------------------------------------- #



# ----------------- b) Erro Médio Quadrático: --------------- #
def emq(f, g):
    
    # Quadrado das diferenças entre as matrizes
    diferenca_quadrada = (f - g) ** 2
    
    # Soma das diferenças quadradas
    soma_diferencas_quadradas = np.sum(diferenca_quadrada)
    
    # Número total de elementos na matriz
    total_elementos = f.size
    
    # EMQ
    emq = soma_diferencas_quadradas / total_elementos
    
    return emq
# ----------------------------------------------------------- #



# ----------------- c) Erro Médio Quadrático Normalizado: --- #
def emqn(f, g):

    # EMQ
    EMQ = emq(f, g)
    
    # Desvio padrão dos valores em M1
    desvio_padrao = np.std(f)
    
    # EMQN
    emqn = np.sqrt(EMQ) / desvio_padrao if desvio_padrao != 0 else 0

    return emqn
# ----------------------------------------------------------- #



# ----------------- d) Média: ------------------------------- #
def media(f, g):

    # Média da matriz F (𝜇𝐹 ) e da matriz G (𝜇𝐺)
    media_f = np.mean(f)
    media_g = np.mean(g)
    
    return media_f, media_g
# ----------------------------------------------------------- #



# ----------------- e) Variância: --------------------------- #
def variancia(f, g):

    # Variância da matriz F (𝜎𝐹 ) e da matriz G (𝜎𝐺)
    variancia_f = np.var(f)
    variancia_g = np.var(g)
    
    return variancia_f, variancia_g
# ----------------------------------------------------------- #



# ----------------- f) Covariância: ------------------------- #
def covariancia(f, g):

    # Achatar as matrizes para vetores
    f_flat = f.flatten()
    g_flat = g.flatten()
    
    # Covariância entre os vetores
    covariancia = np.cov(f_flat, g_flat)[0, 1]
    
    return covariancia
# ----------------------------------------------------------- #



# ----------------- g) oeficiente de Correlação: ------------ #
def correlacao(f, g):

    # Achatar as matrizes para vetores
    f_flat = f.flatten()
    g_flat = g.flatten()
    
    # Coeficiente de correlação entre os vetores
    coeficiente_correlacao = np.corrcoef(f_flat, g_flat)[0, 1]
    
    return coeficiente_correlacao
# ----------------------------------------------------------- #
