# Importa bibliotecas
import os
import platform

# ------------------------ Interface ------------------------ #
def interface():
    # Verifica o sistema operacional
    comando = 'cls' if platform.system() == "Windows" else 'clear'
    
    # Limpa o sistema
    os.system(comando)
# ----------------------------------------------------------- #