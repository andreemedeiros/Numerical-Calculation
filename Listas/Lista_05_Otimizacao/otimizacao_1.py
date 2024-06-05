# ----------------------------------------------------------- #
# Lista 05 - Otimização                                       #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Métodos da Razão Áurea e Interpolação Quadrática.
# Função: 𝑓 (𝑥) = −(1.5)^6 −2𝑥^4 + 12𝑥
# a) Gráfico da função.
# b) Valor de 𝑥 que maximiza a função 𝑓 (𝑥) com Busca da razão áurea. 𝑥𝑖 = 0 e 𝑥𝑓 = 2.
# c) Interpolação quadrática com 𝑥1 = 0, 𝑥2 = 1 e 𝑥3 = 2.

import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return -(1.5)**6 - 2*x**4 + 12*x

# a) Gráfico da função
x = np.linspace(0, 2, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = -(1.5)^6 - 2x^4 + 12x')
plt.title('Gráfico da Função f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

# b) Busca da Razão Áurea
def golden_ratio_search(f, xi, xf, tol=1e-5):
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

# Encontrando o valor de x que maximiza f(x)
xi = 0
xf = 2
x_max = golden_ratio_search(f, xi, xf)
print(f"Valor de x que maximiza f(x) usando busca da razão áurea: {x_max:.5f}")

# c) Interpolação Quadrática
def quadratic_interpolation(f, x1, x2, x3, tol=1e-5):
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
x1 = 0
x2 = 1
x3 = 2
x_max_quad = quadratic_interpolation(f, x1, x2, x3)
print(f"Valor de x que maximiza f(x) usando interpolação quadrática: {x_max_quad:.5f}")
