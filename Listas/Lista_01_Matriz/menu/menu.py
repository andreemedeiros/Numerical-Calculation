# Menu para escolha das operações:
# a) Erro Médio Absoluto;
# b) Erro Médio Quadrático;
# c) Erro Médio Quadrático Normalizado;
# d) Média;
# e) Variância;
# f) Covariância;
# g) oeficiente de Correlação.

from menu.interface import interface
from funcoes.funcoes import ema
from funcoes.funcoes import emq
from funcoes.funcoes import emqn
from funcoes.funcoes import media
from funcoes.funcoes import variancia
from funcoes.funcoes import covariancia
from funcoes.funcoes import correlacao

# ------------------------ Menu ------------------------ #
def menu(F,G):
    # Escolher Operação:
    opc = int(input("Qual operação realizar? \n-------------------------\n 1: EMA\n 2: EMQ\n 3: EMQN\n 4: Média\n 5: Variância\n 6: Covariância\n 7: Coeficiente de Correlação\n -------------------------\n 8: Encerrar\n-------------------------\n"))

    if opc == 1:
        # a) EMA:
        interface()
        EMA = ema(F, G)
        print(f"\na)Erro Médio Absoluto (EMA) entre as matrizes F e G: \n {EMA} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)
    elif opc == 2:
        # b) EMQ:
        interface()
        EMQ = emq(F, G)
        print(f"\nb) Erro Médio Quadrático (EMQ) entre as matrizes F e G: \n {EMQ} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)
    elif opc == 3:
        # c) EMQN:
        interface()
        EMQN = emqn(F, G)   
        print(f"\nc) Erro Médio Quadrático Normalizado (EMQN) entre as matrizes F e G: \n {EMQN} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)
    elif opc == 4:
        # d) Média:
        interface()
        media_F, media_G = media(F, G)
        print(f"\nd) Média de F (𝜇𝐹): {media_F}")
        print(f"\nd) Média de G (𝜇𝐺): {media_G} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)    
        pass
    elif opc == 5:
        # e) Variância:
        interface()
        variancia_F, variancia_G = variancia(F, G)
        print(f"\ne) Variância de F (𝜎𝐹): {variancia_F}")
        print(f"\ne) Variância de G (𝜎𝐺): {variancia_G} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)
        pass
    elif opc == 6:
        # f) Covariância:
        interface()
        covariancia_F_G = covariancia(F, G)
        print(f"\nCovariância entre F e G: \n {covariancia_F_G} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G) 
        pass
    elif opc == 7:
        # g) Coeficiente de Correlação:
        interface()
        coeficiente_correlacao_F_G = correlacao(F, G)
        print(f"\nCoeficiente de correlação entre F e G: \n {coeficiente_correlacao_F_G} \n")
        input("Pressione Enter para continuar...")
        interface()
        menu(F,G)
        pass
    elif opc == 8:
        # Encerrar:
        interface()
        input("Fechando programa...")
        pass
    else:
        # Tratamento de erro:
        interface()
        input("Selecione um valor válido. ")
        interface()
        menu(F,G)
        pass
# ----------------------------------------------------------- #