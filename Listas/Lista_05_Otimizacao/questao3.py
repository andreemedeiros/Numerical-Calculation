# Métodos de Razão Áurea e Interpolação Quadrática.
# Função: 𝑓 (𝑥) = 𝑥^4 + 2𝑥^3 + 8𝑥^2 + 5𝑥
# a) Gráfico do mínimo para algum valor de 𝑥 no intervalo entre −2 ≤𝑥 ≤1.
# b) Mínimo da função usando busca da razão áurea (𝑥𝑖 = −2 e 𝑥𝑓 = 1, com erro absoluto < 0.5%).
# c) Mínimo da função usando interpolação quadrática (𝑥1 = −2 e 𝑥2 = −1 e 𝑥3 = 1, com erro absoluto < 0.5%).

import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return x**4 + 2*x**3 + 8*x**2 + 5*x

# a) Gráfico da Função
x_values = np.linspace(-2, 1, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = x^4 + 2x^3 + 8x^2 + 5x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função f(x)')
plt.grid(True)
plt.legend()
plt.show()

# b) Busca da Razão Áurea
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

# Encontrando o mínimo usando busca da razão áurea
xi = -2
xf = 1
x_min_gr = golden_ratio_search(f, xi, xf)
print(f"Mínimo da função usando busca da razão áurea: {x_min_gr:.5f}")

# c) Interpolação Quadrática
def quadratic_interpolation(f, x1, x2, x3, tol=0.005):
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

# Encontrando o mínimo usando interpolação quadrática
x1 = -2
x2 = -1
x3 = 1
x_min_quad = quadratic_interpolation(f, x1, x2, x3)
print(f"Mínimo da função usando interpolação quadrática: {x_min_quad:.5f}")
