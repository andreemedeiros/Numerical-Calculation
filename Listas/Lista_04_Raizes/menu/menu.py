import sys

from menu.interface import interface

# Menu para questões 
def menu():

  opcao = int(input("Escolha uma opção: \n-------------------------\n 1 - Questão 01:  método da Bisseção \n-------------------------\n 2 - Questão 02: método da Falsa Posição \n-------------------------\n 3 - Questão 03: método da Secante \n-------------------------\n 4 - Questão 04: método da Secante Modificado \n-------------------------\n 0 - Sair \n-------------------------\n Opção: "))

  if opcao == 1:
    interface()
    from questoes.q1_biseccao import testes_biseccao
    input("Pressione Enter para continuar...")
    interface()
    menu()
  if opcao == 2:
    interface()
    from questoes.q2_fposicao import testes_fposicao
    input("Pressione Enter para continuar...")
    interface()
    menu()
  if opcao == 3:
    interface()
    from questoes.q3_secante import testes_secante
    input("Pressione Enter para continuar...")
    interface()
    menu()
  if opcao == 4:
    interface()
    from questoes.q4_msecante import testes_msecante
    input("Pressione Enter para continuar...")
    interface()
    menu()
  elif opcao == 0:
    interface()
    print("Encerrando o programa...")
    interface()
  else:
    interface()
    input("Opção inválida. Por favor, escolha uma opção válida.")
    interface()
    menu()
