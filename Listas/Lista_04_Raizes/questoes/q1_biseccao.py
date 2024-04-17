import math

# Definindo a função de bisseção
def bissecao(funcao, xa, xb, n_int, best_apro):
    # Impressão inicial do cabeçalho
    print("Metodo da Bissecao")
    print("----------------------------------------------------------------")
    print("Int    xa           xb           erro_abs            erro_rel")
    print("----------------------------------------------------------------")
    
    # Loop para realizar as iterações
    for i in range(1, n_int + 1):
        # Calculando a média entre xa e xb como a nova raiz xr
        xr = (xa + xb) / 2
        
        # Calculando erros
        erro_abs = abs(xr - best_apro)
        erro_rel = abs(erro_abs / xr)
        
        # Impressão dos resultados da iteração atual
        print(f"{i}    {xa:.10f}    {xb:.10f}    {erro_abs:.14f}    {erro_rel:.14f}")
        
        # Atualização dos limites xa e xb baseado no valor da função em xr
        if funcao(xa) * funcao(xr) < 0:
            xb = xr
        elif funcao(xa) * funcao(xr) > 0:
            xa = xr
        else:
            break
            
    # Impressão dos resultados finais
    print("FIM")
    print(f"Funcao___________: {funcao.__name__}")
    print(f"Raiz encontrada__: {xr}")
    print(f"Erro absoluto____: {erro_abs}")
    print(f"Erro relativo____: {erro_rel}")
    
    return xr, erro_rel, erro_abs

# Definindo as funções fornecidas
def funcao_a(x):
    return 3*x**2 + 2*x - 2

def funcao_b(x):
    return 2*x**3 + x**2 + 2*x - 1

def funcao_c(x):
    return x**3 + 2*x - 30

def funcao_d(x):
    return 4 - x - x**2

# Lista de testes com as funções, intervalos e melhores aproximações
testes_biseccao = [
    (funcao_a, 0, 1, 0.5),
    (funcao_b, 0, 1, 0.5),
    (funcao_c, 2, 3, 2.5),
    (funcao_d, -2, 1, 0)
]

# Execução dos testes
for funcao, xa, xb, best_apro in testes_biseccao:
    print("\n===========================================")
    bissecao(funcao, xa, xb, 10, best_apro)
