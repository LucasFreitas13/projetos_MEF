from src.fem.montagem import montar_matriz_rigidez_barra_1D

K = montar_matriz_rigidez_barra_1D(4, 200e9, 0.01, 1.0)
print(K)