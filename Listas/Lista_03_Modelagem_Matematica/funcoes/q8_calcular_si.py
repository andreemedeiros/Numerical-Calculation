import math

def calcular_serie_infinita(a, numero_de_iteracoes):
  """
  Calcula a soma da série infinita ∑_(n=1)^∞ (a^n) / n^4.

  Args:
    a: O valor de a.
    numero_de_iteracoes: O número MÁXIMO de iterações (para evitar estouro).

  Returns:
    A soma da série infinita.
  """

  soma = 0.0
  termo_anterior = 0.0
  erro_relativo = 1.0

  for n in range(1, numero_de_iteracoes + 1):
    try:
      # Tenta calcular o fatorial usando a função gamma
      fatorial_n4 = math.gamma(n**4 + 1)
      termo = (a**n) / fatorial_n4
    except OverflowError:
      # Se ocorrer estouro, limita o cálculo e avisa o usuário
      print(f"Atenção: O número de iterações foi limitado para evitar estouro.")
      break

    soma += termo
    erro_relativo = 0.0 if termo_anterior == 0 else abs((soma - termo_anterior) / termo_anterior)
    termo_anterior = soma

  print(f"Soma da série infinita com a = {a:.2f} e {numero_de_iteracoes} iterações: {soma:.4f}")
  print(f"Erro relativo: {erro_relativo:.4f}")

  return soma

a = float(input("Digite o valor de a: "))
numero_de_iteracoes = int(input("Digite o número MÁXIMO de iterações (para evitar estouro): "))

calcular_serie_infinita(a, numero_de_iteracoes)
