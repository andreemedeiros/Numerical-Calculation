# Função para gerar as matrizes 𝐹[𝑖][𝑗] e 𝐺[𝑖][𝑗]
# onde, 𝑖 = (1,2,...,𝑛) e 𝑗 = (1,2,...,𝑛) 
# usando a função rand com valores entre 0 e 100.

import numpy as np

from menu.interface import interface

# Questão 1:
# ------------------ Função criar matrizes ------------------ #
def matriz():

    n = int(input("Insira a dimensão n para as matrizes F e G: "))
    
    # Gera as matrizes F e G com valores inteiros aleatórios entre 0 e 100
    f = np.random.randint(0, 101, size=(n, n))
    g = np.random.randint(0, 101, size=(n, n))
    
    print(f"Matriz F:\n {f}")
    print(f"\nMatriz G:\n {g}")
    
    input("Pressione Enter para continuar...")
    interface()

    return f, g
# ----------------------------------------------------------- #