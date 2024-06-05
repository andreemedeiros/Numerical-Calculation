# ----------------------------------------------------------- #
# Lista 05 - Otimização                                       #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Métodos de Razão Áurea e Interpolação Quadrática.
# Função: 𝑓 (𝑥) = 4𝑥 −1.8𝑥^2 + 1.2^3 −0.3^4
# a) Busca da razão áurea (𝑥𝑖 = −2 e 𝑥𝑓 = 4, com erro absoluto < 1%).
# b) Interpolação quadrática (𝑥1 = 1.75 e 𝑥2 = 2 e 𝑥3 = 2.5, com erro absoluto < 1%). 

import numpy as np

# Definindo a função
def f(x):
    return 4*x - 1.8*x**2 + 1.2**3 - 0.3**4

# a) Busca da Razão Áurea
def golden_ratio_search(f, xi, xf, tol=1e-2):
    gr = (np.sqrt(5) - 1) / 2
    x1 = xf - gr * (xf - xi)
    x2 = xi + gr * (xf - xi)
    
    while abs(xf - xi) > tol:
        if f(x1) < f(x2):
            xf = x2
            x2 = x1
            x1 = xf - gr * (xf - xi)
        else:
            xi = x1
            x1 = x2
            x2 = xi + gr * (xf - xi)
    
    return (xi + xf) / 2

# Encontrando o valor de x que maximiza f(x) usando busca da razão áurea
xi = -2
xf = 4
x_max = golden_ratio_search(f, xi, xf)
print(f"Valor de x que maximiza f(x) usando busca da razão áurea: {x_max:.5f}")

# b) Interpolação Quadrática
def quadratic_interpolation(f, x1, x2, x3, tol=1e-2):
    while abs(x3 - x1) > tol:
        f1, f2, f3 = f(x1), f(x2), f(x3)
        
        a0 = f1
        a1 = (f2 - f1) / (x2 - x1)
        a2 = ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)) / (x3 - x2)
        
        x_opt = (x1 + x2 - a1/a2) / 2
        
        if a2 > 0:
            x3 = x_opt
        else:
            x1 = x_opt
        
        x1, x2, x3 = sorted([x1, x2, x3], key=f)
        
    return x_opt

# Encontrando o valor de x que maximiza f(x) usando interpolação quadrática
x1 = 1.75
x2 = 2
x3 = 2.5
x_max_quad = quadratic_interpolation(f, x1, x2, x3)
print(f"Valor de x que maximiza f(x) usando interpolação quadrática: {x_max_quad:.5f}")
