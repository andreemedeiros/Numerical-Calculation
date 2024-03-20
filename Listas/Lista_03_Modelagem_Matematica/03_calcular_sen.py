import math

def calcular_sen(x, numero_de_iteracoes):
  """
  Calcula a aproximação de sen(x) usando a série de Taylor.

  Args:
    x: O valor de x.
    numero_de_iteracoes: O número de iterações da série de Taylor.

  Returns:
    A aproximação de sen(x).
  """

  soma = 0.0
  termo_anterior = 0.0
  erro_relativo = 0.0

  for n in range(1, numero_de_iteracoes + 1):
    termo = ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
    soma += termo
    erro_relativo = 0.0 if termo_anterior == 0 else abs((soma - termo_anterior) / termo_anterior)
    termo_anterior = soma

  print(f"Aproximação de sen({x:.2f}) com {numero_de_iteracoes} iterações: {soma:.4f}")
  print(f"Erro relativo: {erro_relativo:.4f}")

  return soma

x = float(input("Digite o valor de x: "))
numero_de_iteracoes = int(input("Digite o número de iterações: "))

calcular_sen(x, numero_de_iteracoes)
