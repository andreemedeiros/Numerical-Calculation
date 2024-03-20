
import math

def calcular_ex(x, numero_de_iteracoes):
  """
  Calcula a aproximação de e^x usando a série de Taylor.

  Args:
    x: O valor de x.
    numero_de_iteracoes: O número de iterações da série de Taylor.

  Returns:
    A aproximação de e^x.
  """

  soma = 1.0
  termo_anterior = 1.0
  erro_relativo = 1.0

  for n in range(1, numero_de_iteracoes + 1):
    termo = (x**n) / math.factorial(n)
    soma += termo
    erro_relativo = abs((soma - termo_anterior) / termo_anterior)
    termo_anterior = soma

  print(f"Aproximação de e^{x:.2f} com {numero_de_iteracoes} iterações: {soma:.4f}")
  print(f"Erro relativo: {erro_relativo:.4f}")

  return soma

x = float(input("Digite o valor de x: "))
numero_de_iteracoes = int(input("Digite o número de iterações: "))

calcular_ex(x, numero_de_iteracoes)
