# ----------------------------------------------------------- #
# Lista 03 - Modelagem Matemática                             #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
import sys

sys.path.append('funcoes')  # Adiciona o diretório 'funcoes' ao PATH

# Menu para questões 
def menu():
  print("Escolha uma opção:")
  print("1 - Questão 01: Calcular pi")
  print("2 - Questão 02: Calcular e^x")
  print("3 - Questão 03: Calcular sen(x)")
  print("4 - Questão 04: Calcular cos(x)")
  print("5 - Questão 05: Calcular senh(x)")
  print("6 - Questão 06: Calcular cosh(x)")
  print("7 - Questão 07: Calcular pi de n")
  print("8 - Questão 08: Calcular série infinita")
  print("0 - Sair")

def main():

    menu()
    opcao = int(input("Opção: "))

    if opcao == 1:
        from funcoes.q1_calcular_pi import calcular_pi
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 2:
        from funcoes.q2_calcular_ex import calcular_ex
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 3:
        from funcoes.q3_calcular_sen import calcular_sen
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 4:
        from funcoes.q4_calcular_cos import calcular_cos
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 5:
        from funcoes.q5_calcular_senh import calcular_senh
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 6:
        from funcoes.q6_calcular_cosh import calcular_cosh
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 7:
        from funcoes.q7_calcular_pin import calcular_pin 
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 8:
        from funcoes.q8_calcular_si import calcular_serie_infinita
        input("Pressione Enter para continuar...")
        main()
    elif opcao == 0:
        print("Encerrando o programa...")
        pass
    else:
        input("Opção inválida. Por favor, escolha uma opção válida.")
        main()

# Inicia programa
main()