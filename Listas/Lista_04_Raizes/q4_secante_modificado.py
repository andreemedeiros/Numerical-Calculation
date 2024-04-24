# Método da Secante Modificado
# a) 𝑓 (𝑥) = 2^(𝑥^2) −4𝑥. Ponto: 𝑥𝑖 = −0.5
# b) 𝑓 (𝑥) = 4^(𝑥^2) −6𝑥. Ponto: 𝑥𝑖 = 1.5

def secantemod(funcao, xi, d, int, best_apro):
    print("Metodo da Secante Modificado")
    print("----------------------------------------------------------------")
    print("Int\t\txi\t\t\t\terro_abs\t\terro_rel")
    print("----------------------------------------------------------------")
    
    for i in range(1, int+1):
        fxim1 = funcao(xi - d)
        fxi = funcao(xi)
        
        # Verifica se fxim1 e fxi são iguais para evitar divisão por zero
        if fxim1 == fxi:
            print("Divisão por zero evitada.")
            break
        
        xr = xi - (d * fxi) / (fxi - fxim1)  # Fórmula da Secante Modificada
        
        # Erro absoluto e relativo
        erro_abs = abs(xr - best_apro)
        erro_rel = erro_abs / abs(xr)
        
        print(f"{i}\t\t{xi:.10f}\t\t{erro_abs:.14f}\t\t{erro_rel:.14f}")
        
        xi = xr
        
        best_apro = xr
    
    print("FIM")
    print(f"Funcao___________: {funcao.__name__}")
    print(f"Raiz encontrada__: {best_apro}")
    print(f"Erro absoluto____: {erro_abs}")
    print(f"Erro relativo____: {erro_rel}")
    
    return best_apro, erro_rel, erro_abs

# Funções para teste
def f1(x):
    return 2**(x**2) - 4*x

def f2(x):
    return 4**(x**2) - 6*x

# Testes
print("\nTeste para f(x) = 2^(x^2) - 4x")
secantemod(f1, -0.5, 0.01, 10, 0)

print("\nTeste para f(x) = 4^(x^2) - 6x")
secantemod(f2, 1.5, 0.01, 10, 0)
