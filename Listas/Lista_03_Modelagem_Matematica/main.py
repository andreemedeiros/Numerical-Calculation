# ----------------------------------------------------------- #
# Lista 03 - Modelagem Matemática                             #
# Autor         : André Medeiros                              #
# Criação       : 20/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #

import sys

sys.path.append('funcoes')  # Adiciona o diretório 'funcoes' ao PATH

from funcoes.q1_calcular_pi import calcular_pi
from funcoes.q2_calcular_ex import calcular_ex
from funcoes.q3_calcular_sen import calcular_sen
from funcoes.q4_calcular_cos import calcular_cos
from funcoes.q5_calcular_senh import calcular_senh
from funcoes.q6_calcular_cosh import calcular_cosh
from funcoes.q7_calcular_pi import calcular_pi
from funcoes.q8_calcular_si import calcular_serie_infinita

def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Calcular pi")
    print("2 - Calcular e^x")
    print("0 - Sair")

def main():
        exibir_menu()
        opcao = int(input("Qual operação realizar? \n-------------------------\n 1: EMA\n 2: EMQ\n 3: EMQN\n 4: Média\n 5: Variância\n 6: Covariância\n 7: Coeficiente de Correlação\n -------------------------\n 8: Encerrar\n-------------------------\n"))


        if opcao == 1:
            input("1111.")
            calcular_pi()
            input("Pressione Enter para continuar...")
            pass
        elif opcao == 2:
            input("22222222")
            calcular_ex()
            input("Pressione Enter para continuar...")
            pass
        elif opcao == 0:
            input("33333")
            calcular_sen()
            input("Pressione Enter para continuar...")
            pass
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            pass

if __name__ == "__main__":
    main()
