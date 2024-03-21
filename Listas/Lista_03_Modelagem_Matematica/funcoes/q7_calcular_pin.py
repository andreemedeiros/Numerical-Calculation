import math

def calcular_pin(numero_de_iteracoes):
  """
  Calcula a aproximação de π usando a série de Madhava-Leibniz.

  Args:
    numero_de_iteracoes: O número de iterações da série de Madhava-Leibniz.

  Returns:
    A aproximação de π.
  """

  soma = 0.0
  termo = 4.0 / 1.0
  erro_relativo = 1.0

  for n in range(1, numero_de_iteracoes + 1):
    soma += termo
    termo *= -1.0 * (4.0 * n) / ((4.0 * n) + 2.0)
    erro_relativo = abs((soma - termo) / soma)

  print(f"Aproximação de π com {numero_de_iteracoes} iterações: {soma:.4f}")
  print(f"Erro relativo: {erro_relativo:.4f}")

  return soma

numero_de_iteracoes = int(input("Digite o número de iterações: "))

calcular_pin(numero_de_iteracoes)
