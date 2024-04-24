# Solução exercício 13.1 

import numpy as np

# Definindo os valores de x e y
x = np.array([0, 1, 2.5, 3, 4.5, 5, 6])
y = np.array([2, 5.4375, 7.3516, 7.5625, 8.4453, 9.1875, 12])

# Criando a tabela de diferenças divididas finitas
n = len(x)
diff_div = np.zeros((n, n))

# Diferenças divididas de primeira ordem
diff_div[:, 0] = y

# Diferenças divididas de ordens superiores
for i in range(1, n):
    for j in range(n-i):
        diff_div[j, i] = (diff_div[j+1, i-1] - diff_div[j, i-1]) / (x[j+i] - x[j])

# Função para calcular o valor de y em um ponto x usando o polinômio de Newton
def newton_polynomial(x, x_data, y_data, diff_div):
    n = len(x_data)
    result = y_data[0]

    for i in range(1, n):
        term = diff_div[0, i]
        for j in range(1, i+1):
            term *= (x - x_data[j])
        result += term

    return result

# Calculando o valor de y em x = 3.5
x_target = 3.5
y_interpolated = newton_polynomial(x_target, x, y, diff_div)

print("Valor interpolado de y em x = 3.5:", y_interpolated)
