# Função em Python capaz de calcular a aproximação de uma raiz usando
# o método da Secante Modificado
# a) 𝑓(𝑥) = 2𝑥^2 − 4𝑥. Ponto: 𝑥𝑖 = −0.5
# b) 𝑓(𝑥) = 4𝑥^2 − 6𝑥. Ponto: 𝑥𝑖 = 1.5

import math

def secantemod(funcao, xi, d, n_int, best_apro):
    print("Metodo da Secante Modificado")
    print("----------------------------------------------------------------")
    print("Int    xi           erro_abs            erro_rel")
    print("----------------------------------------------------------------")
    
    xr = xi  # Inicializando xr antes do loop
    erro_abs = 0  # Inicializando erro_abs
    erro_rel = 0  # Inicializando erro_rel
    
    for i in range(1, n_int + 1):
        fx = funcao(xi)
        xim1 = xi - d * fx
        
        fxim1 = funcao(xim1)
        
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
        
        print(f"{i}    {xi:.10f}    {erro_abs:.14f}    {erro_rel:.14f}")
        
        xi = xr
            
    print("FIM")
    print(f"Funcao___________: {funcao.__name__}")
    
    if 'xr' in locals():
        print(f"Raiz encontrada__: {xr}")
        print(f"Erro absoluto____: {erro_abs}")
        print(f"Erro relativo____: {erro_rel}")
    else:
        print("Raiz não encontrada.")
    
    return xr, erro_rel, erro_abs

# Funções fornecidas
def funcao_a(x):
    return 2*x**2 - 4*x

def funcao_b(x):
    return 4*x**2 - 6*x

# Lista de testes
testes_msecante = [
    (funcao_a, -0.5, 0.01, 10, 0),
    (funcao_b, 1.5, 0.01, 10, 1)
]

# Execução dos testes
for funcao, xi, d, n_int, best_apro in testes_msecante:
    print("\n===========================================")
    secantemod(funcao, xi, d, n_int, best_apro)
