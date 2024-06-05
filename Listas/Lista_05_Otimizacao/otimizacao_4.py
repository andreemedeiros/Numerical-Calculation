# ----------------------------------------------------------- #
# Lista 05 - Otimização                                       #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Métodos de Razão Áurea e Interpolação Quadrática.
# Função: 𝑦 = 6cos(𝑥) − 1.5sen(𝑥)
# a) Gráfico da função
# b) Valor que minimiza
# c) Pressão mínima

import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return 6 * np.cos(x) - 1.5 * np.sin(x)

# Método da Razão Áurea para encontrar o mínimo
def golden_ratio_search(f, xi, xf, tol=0.005):
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

# Encontrando o valor de x que minimiza a função usando a razão áurea
xi = 2
xf = 4
x_min = golden_ratio_search(f, xi, xf)
y_min = f(x_min)

print(f"Valor de x que minimiza a função: {x_min:.5f}")
print(f"Pressão mínima: {y_min:.5f}")

# Plotando o gráfico da função
x_values = np.linspace(0, 6, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='y = 6cos(x) - 1.5sin(x)')
plt.scatter(x_min, y_min, color='red', label=f'Min: ({x_min:.5f}, {y_min:.5f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função y = 6cos(x) - 1.5sin(x)')
plt.grid(True)
plt.legend()
plt.show()
