# ----------------------------------------------------------- #
# Lista 07 - Integração                                       #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Solução da lista 07 - Integração

import numpy as np

# Definição das funções das integrais de cada função

# Função 27
def f27(x):
  return 1 - np.exp(-2 * x)

# Função 28
def f28(x):
  return 6 + 3 * np.cos(x)

# Função 29
def f29(x):
  return ( 1 - x - 4 * x**3 + 2 * x**5 )

# Função 30
def f30(x):
  return ( (4 * x - 3)**3 )

# Função 31
def f31(x):
  return ( 5 + 3 * np.cos(x) )

# Função 32
def f32(x):
  return ( 14**(2*x) )

# ----------------------------------------------------------
# Função de calcular a integral pelo método do trapézio
def trapezio_simples(f, a, b, n):
  """
  Aproxima a integral definida de 'f' usando a regra dos trapézios simples com 'n' pontos.

  Parâmetros:
    f: Função a ser integrada.
    a: Limite inferior de integração.
    b: Limite superior de integração.
    n: Número de pontos de integração (incluindo os limites).

  Retorno:
    Valor aproximado da integral.
  """

  h = (b - a) / n 
  soma = 0
  for i in range(1, n):
    soma += f(a + i * h)
  soma *= 2
  soma += (f(a) + f(b))
  return (h / 2) * soma  
# ----------------------------------------------------------

# Limite das funções das questões

a_27 = 0  # Limite inferior da função 27
b_27 = 4  # Limite superior da função 27

a_28 = 0        # Limite inferior da função 28
b_28 = np.pi/2  # Limite superior da função 28

a_29 = -2 # Limite inferior da função 29
b_29 = 4  # Limite superior da função 29

a_30 = -3 # Limite inferior da função 30
b_30 = 5  # Limite superior da função 30

a_31 = 0  # Limite inferior da função 31
b_31 = 3  # Limite superior da função 31

a_32 = 0.5  # Limite inferior da função 32
b_32 = 1.5  # Limite superior da função 32

n = 5  # Número de pontos (sempre 5)

# Calculando as integrais de cada função
integral_f27 = trapezio_simples(f27, a_27, b_27, n)
integral_f28 = trapezio_simples(f28, a_28, b_28, n)
integral_f29 = trapezio_simples(f29, a_29, b_29, n)
integral_f30 = trapezio_simples(f30, a_30, b_30, n)
integral_f31 = trapezio_simples(f31, a_31, b_31, n)
integral_f32 = trapezio_simples(f32, a_32, b_32, n)

# Mostrando os resultados de cada função
print("Integral da função 27:", integral_f27)
print("Integral da função 28:", integral_f28)
print("Integral da função 29:", integral_f29)
print("Integral da função 30:", integral_f30)
print("Integral da função 31:", integral_f31)
print("Integral da função 32:", integral_f32)
