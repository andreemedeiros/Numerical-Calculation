import math

def fposicao(funcao, xa, xb, n_int, best_apro):
    print("Metodo da Falsa Posicao")
    print("----------------------------------------------------------------")
    print("Int    xa           xb           erro_abs            erro_rel")
    print("----------------------------------------------------------------")
    
    for i in range(1, n_int + 1):
        xr = xb - (funcao(xb) * (xb - xa)) / (funcao(xb) - funcao(xa))
        
        erro_abs = abs(xr - best_apro)
        erro_rel = abs(erro_abs / xr)
        
        print(f"{i}    {xa:.10f}    {xb:.10f}    {erro_abs:.14f}    {erro_rel:.14f}")
        
        if funcao(xa) * funcao(xr) < 0:
            xb = xr
        elif funcao(xa) * funcao(xr) > 0:
            xa = xr
        else:
            break
            
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
    return 3*x**2 + 2*x - 2

def funcao_c(x):
    return 2*x**3 + x**2 + 2*x - 1

def funcao_d(x):
    return x**3 + 2*x - 30

def funcao_e(x):
    return 4*x**2 - 5*x - 3

# Lista de testes
testes_fposicao = [
    (funcao_a, -0.5, 0.5, 10, 0),
    (funcao_b, 0, 1, 10, 0.5),
    (funcao_c, 0, 1, 10, 0.5),
    (funcao_d, 2, 3, 10, 2.5),
    (funcao_e, -0.25, 0.15, 10, 0)
]

# Execução dos testes
for funcao, xa, xb, n_int, best_apro in testes_fposicao:
    print("\n===========================================")
    fposicao(funcao, xa, xb, n_int, best_apro)
