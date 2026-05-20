import numpy as np
from src.fem.posprocessamento import plotar_resultados


L = 1.0          # comprimento [m]
E = 210e9        # módulo de elasticidade [Pa]
A = 0.01         # área [m²]

# Vetor de deslocamentos 
u = np.array([0.0, 0.005, 0.01])  # [m]

plotar_resultados(u, L, E, A)