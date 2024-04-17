# Função em Python capaz de calcular a aproximação de uma raiz usando 
# o método da Secante.
# a) 𝑓(𝑥) = 2𝑥^2 − 4𝑥. Pontos: 𝑥0 = −0.5 e 𝑥1 = −1.
# b) 𝑓(𝑥) = 4𝑥^2 − 6𝑥. Pontos: 𝑥0 = 1.5 e 𝑥1 = 2.

import math

def secante(funcao, xi, xim1, n_int, best_apro):
    print("Metodo da Secante")
    print("----------------------------------------------------------------")
    print("Int    xi           xim1         erro_abs            erro_rel")
    print("----------------------------------------------------------------")
    
    for i in range(1, n_int + 1):
        fxim1 = funcao(xim1)
        fx = funcao(xi)
        
        # Verificando se o denominador é zero
        if fxim1 == fx:
            print(f"Divisão por zero encontrada na iteração {i}.")
            break
        
        xr = xi - (fx * (xi - xim1)) / (fx - fxim1)
        
        erro_abs = abs(xr - best_apro)
        
        # Verificando se xr é muito próximo de zero
        if abs(xr) > 1e-10:
            erro_rel = abs(erro_abs / xr)
        else:
            erro_rel = 0
        
        print(f"{i}    {xi:.10f}    {xim1:.10f}    {erro_abs:.14f}    {erro_rel:.14f}")
        
        xim1 = xi
        xi = xr
            
    print("FIM")
    print(f"Funcao___________: {funcao.__name__}")
    print(f"Raiz encontrada__: {xr}")
    print(f"Erro absoluto____: {erro_abs}")
    print(f"Erro relativo____: {erro_rel}")
    
    return xr, erro_rel, erro_abs

# Funções fornecidas
def funcao_a(x):
    return 2*x**2 - 4*x

def funcao_b(x):
    return 4*x**2 - 6*x

# Lista de testes
testes_secante = [
    (funcao_a, -0.5, -1, 10, 0),
    (funcao_b, 1.5, 2, 10, 1)
]

# Execução dos testes
for funcao, xi, xim1, n_int, best_apro in testes_secante:
    print("\n===========================================")
    secante(funcao, xi, xim1, n_int, best_apro)
