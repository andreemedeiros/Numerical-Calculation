

import math
import matplotlib.pyplot as plt

def calcular_pi(numero_de_iteracoes):
  """
  Calcula o valor de pi usando a série infinita da Equação 10.19.

  Args:
    numero_de_iteracoes: O número de iterações da série infinita.

  Returns:
    O valor de pi.
  """

  soma = 0.0
  erro_relativo = 1.0
  erros_relativos = []

  for n in range(1, numero_de_iteracoes + 1):
    termo = 1 / ((2 * n)**2 * (2 * n - 1) * (2 * n + 1))
    soma += termo
    erro_relativo = abs((soma - math.pi) / math.pi)
    erros_relativos.append(erro_relativo)

  print(f"Valor de pi com {numero_de_iteracoes} iterações: {soma}")
  print(f"Erro relativo: {erro_relativo}")

  return soma, erros_relativos

# Solicita o número de iterações ao usuário
numero_de_iteracoes = int(input("Digite o número de iterações: "))

# Calcula o valor de pi e o erro relativo
pi, erros_relativos = calcular_pi(numero_de_iteracoes)

# Exibe o gráfico do erro relativo
plt.plot(list(range(1, numero_de_iteracoes + 1)), erros_relativos)
plt.xlabel("Número de iterações")
plt.ylabel("Erro relativo")
plt.show()
