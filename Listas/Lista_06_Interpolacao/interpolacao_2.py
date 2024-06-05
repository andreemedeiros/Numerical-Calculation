# ----------------------------------------------------------- #
# Lista 06 - Interpolação                                     #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Solução interpolação 2

import numpy as np

# Dados fornecidos
x = np.array([0, 1, 2, 5.5, 11, 13, 16, 18])
y = np.array([0.5, 3.134, 5.3, 9.9, 10.2, 9.35, 7.2, 6.2])

# Calculando as diferenças divididas finitas
def divided_differences(x, y):
    n = len(y)
    coef = np.zeros(n)
    coef[0] = y[0]
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j])
        coef[j] = y[j]
    
    return coef

# Construindo o polinômio interpolador de Newton
def newton_interpolation(x, coef, xi):
    n = len(x) - 1
    p = coef[n]
    
    for k in range(n-1, -1, -1):
        p = coef[k] + (xi - x[k]) * p
    
    return p

# Calculando as diferenças divididas
coef = divided_differences(x, y)

# Avaliando o polinômio interpolador em x = 8
xi = 8
y_interpolated = newton_interpolation(x, coef, xi)

print(f"O valor interpolado de y para x = {xi} é {y_interpolated:.4f}")
