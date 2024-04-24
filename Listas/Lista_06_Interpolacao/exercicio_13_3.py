# Solução exercício 13.3

import numpy as np

# Dados fornecidos
i = np.array([0.25, 0.75, 1.25, 1.5, 2.0])
V = np.array([-0.45, -0.6, 0.70, 1.88, 6.0])

# Interpolação polinomial de quarto grau
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

# Avaliando o polinômio interpolador em i = 1.15
xi = 1.15
V_interpolated = polynomial_interpolation(i, V, xi)

print(f"A estimativa da queda de tensão para i = {xi} é {V_interpolated:.4f}")
