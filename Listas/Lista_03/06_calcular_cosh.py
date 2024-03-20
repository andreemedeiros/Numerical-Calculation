import math

def calcular_cosh(x, numero_de_iteracoes):
  """
  Calcula a aproximação de cosh(x) usando a série de Taylor.

  Args:
    x: O valor de x.
    numero_de_iteracoes: O número de iterações da série de Taylor.

  Returns:
    A aproximação de cosh(x).
  """

  soma = 1.0
  termo_anterior = 1.0
  erro_relativo = 1.0

  for n in range(1, numero_de_iteracoes + 1):
    termo = (x**(2*n)) / math.factorial(2*n)
    soma += termo
    erro_relativo = abs((soma - termo_anterior) / termo_anterior)
    termo_anterior = soma

  print(f"Aproximação de cosh({x:.2f}) com {numero_de_iteracoes} iterações: {soma:.4f}")
  print(f"Erro relativo: {erro_relativo:.4f}")

  return soma

x = float(input("Digite o valor de x: "))
numero_de_iteracoes = int(input("Digite o número de iterações: "))

calcular_cosh(x, numero_de_iteracoes)
