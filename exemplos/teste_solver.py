import numpy as np
from src.fem.solver import resolver_sistema_linear

K = np.array([
    [10, -10],
    [-10, 10]
], dtype=float)

F = np.array([0, 100], dtype=float)

# Condição de contorno
dofs_livres = [1]


# Resolução do sistema
u = resolver_sistema_linear(K, F, dofs_livres)


# Resultados
print("Deslocamentos:")
print(u)

# Valor esperado:
# u = [0, 10]