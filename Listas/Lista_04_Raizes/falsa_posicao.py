# ----------------------------------------------------------- #
# Lista 04 - Raizes                                           #
# Autor         : André Medeiros                              #
# Criação       : 02/03/24                                    #
# E-mail        : andre.escariao1@gmail.com                   #
# ----------------------------------------------------------- #
# Método da Falsa Posição.
# a) 𝑓 (𝑥) = (2^(𝑥^(2))) −4𝑥. Intervalo: 𝑥1 = −0.5 e 𝑥2 = 0.5.
# b) 𝑓 (𝑥) = 3(𝑥^(2)) + 2𝑥 −2. Intervalo 𝑥1 = 0 e 𝑥2 = 1.
# c) 𝑓 (𝑥) = 2(𝑥^(3)) + (𝑥^(2)) + 2𝑥 −1. Intervalo: 𝑥1 = 0 e 𝑥2 = 1.
# d) 𝑓 (𝑥) = (𝑥^(3)) + 2𝑥 −30. Intervalo: 𝑥1 = 2 e 𝑥2 = 3.
# e) 𝑓 (𝑥) = (4^(2𝑥^(2)−5𝑥)) −3. Intervalo: 𝑥1 = −0.25 e 𝑥2 = 0.15.


def fposicao(funcao, xa, xb, int, best_apro):
    print("Metodo da Falsa Posicao")
    print("----------------------------------------------------------------")
    print("Int\t\txa\t\t\t\txb\t\t\t\terro_abs\t\terro_rel")
    print("----------------------------------------------------------------")
    
    for i in range(1, int+1):
        xr = xa - (funcao(xa) * (xb - xa)) / (funcao(xb) - funcao(xa))  # Fórmula da Falsa Posição
        
        # Erro absoluto e relativo
        erro_abs = abs(xr - best_apro)
        erro_rel = erro_abs / abs(xr)
        
        print(f"{i}\t\t{xa:.10f}\t\t{xb:.10f}\t\t{erro_abs:.14f}\t\t{erro_rel:.14f}")
        
        if funcao(xa) * funcao(xr) < 0:
            xb = xr
        else:
            xa = xr
        
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
    return 3*x**2 + 2*x - 2

def f3(x):
    return 2*x**3 + x**2 + 2*x - 1

def f4(x):
    return x**3 + 2*x - 30

def f5(x):
    return 4**(2*x**2 - 5*x) - 3

# Testes
print("\nTeste para f(x) = 2^(x^2) - 4x")
fposicao(f1, -0.5, 0.5, 10, 0)

print("\nTeste para f(x) = 3x^2 + 2x - 2")
fposicao(f2, 0, 1, 10, 0.5)

print("\nTeste para f(x) = 2x^3 + x^2 + 2x - 1")
fposicao(f3, 0, 1, 10, 0.5)

print("\nTeste para f(x) = x^3 + 2x - 30")
fposicao(f4, 2, 3, 10, 2.5)

print("\nTeste para f(x) = 4^(2x^2 - 5x) - 3")
fposicao(f5, -0.25, 0.15, 10, 0)
