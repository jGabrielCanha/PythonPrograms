import matplotlib.pyplot as plt
import numpy as np

def proteina_minima(x):
    return (12 - 0.5*x) / 0.25

def fibra_minima(x):
    return (8 - 0.2*x) / 0.4

def vitamina_minima(x):
    return (6 - 0.1*x) / 0.3

fig, ax = plt.subplots()

x = np.linspace(0, 100, 1000)

# Plotando restrições
ax.plot(x, proteina_minima(x), label="Proteína mínima")
ax.plot(x, fibra_minima(x), label="Fibra mínima")
ax.plot(x, vitamina_minima(x), label="Vitamina mínima")

ax.set_xlim(0, 60)
ax.set_ylim(0, 50)

ax.legend()

ax.set_title("Problema da Dieta")
ax.set_xlabel("Alimento 1")
ax.set_ylabel("Alimento 2")

# Encontrando o ponto ótimo
solucao = np.array([20, 20])
custo_total = 10 * solucao[0] + 20 * solucao[1]

# Plotando o ponto ótimo
ax.plot(solucao[0], solucao[1], 'ro')
ax.annotate(f"Custo total: R${custo_total}", xy=solucao, xytext=(solucao+np.array([5,-5])), 
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()