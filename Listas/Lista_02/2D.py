# Plotagem de gráfico 2D em python com matplotlib

import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
valores = [54, 17, 56, 36, 59, 86]

plt.title('Faturamento no primeiro semestre de 2024')
plt.xlabel('Meses')
plt.ylabel('Faturamento em R$')
plt.plot(meses, valores)
plt.show()
