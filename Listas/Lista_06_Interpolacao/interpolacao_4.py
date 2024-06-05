# ----------------------------------------------------------- #
# Lista 06 - Interpolação                                     #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Solução interpolação 4

import numpy as np

# Dados fornecidos
y = np.array([0, 30000, 60000, 90000, 120000])
g = np.array([9.8100, 9.7487, 9.6879, 9.6278, 9.5682])

# Interpolação polinomial
def polynomial_interpolation(x, y, xi):
    n = len(x)
    P = 0
    
    for j in range(n):
        L = 1
        for m in range(n):
            if m != j:
                L *= (xi - x[m]) / (x[j] - x[m])
        P += y[j] * L
    
    return P

# Avaliando o polinômio interpolador em y = 55000 m
yi = 55000
g_interpolated = polynomial_interpolation(y, g, yi)

print(f"A estimativa da aceleração da gravidade para y = {yi} m é {g_interpolated:.4f} m/s²")
