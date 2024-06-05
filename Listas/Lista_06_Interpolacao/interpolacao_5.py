# ----------------------------------------------------------- #
# Lista 06 - Interpolação                                     #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Solução interpolação 5

import numpy as np

# Dados fornecidos
velocidade = np.array([16, 40, 64, 88, 112])
economia = np.array([4.2, 9.2, 10, 10.7, 8.6])

# Cálculo das diferenças divididas finitas
def divided_differences(x, y):
    n = len(x)
    coef = np.zeros(n)
    coef[0] = y[0]
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j])
        coef[j] = y[j]
    
    return coef

# Avaliação do polinômio interpolador de Newton
def newton_interpolation(x, coef, xi):
    n = len(x)
    P = coef[0]
    temp = 1
    
    for j in range(1, n):
        temp *= (xi - x[j-1])
        P += coef[j] * temp
    
    return P

# Cálculo das diferenças divididas
coef = divided_differences(velocidade, economia)

# Avaliando o polinômio interpolador em 48 km/h
vel = 48
economia_interpolada = newton_interpolation(velocidade, coef, vel)

print(f"A estimativa da economia de combustível para {vel} km/h é {economia_interpolada:.2f} km/l")
