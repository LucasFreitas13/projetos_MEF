import numpy as np
import matplotlib.pyplot as plt

# Entradas do problema
E = 210*10**(9) # [Pa] Mod. Elasticidade
A = 10**(-4) # [²] Área seção transversal
L = 1  # [m] Comprimento da barra
f = 10000 # [N] Força axial
nnos = 10 # Numero de nós

# Discretizacao do comprimento 
l = L/(nnos-1) # Comprimento de cada elemento


k = E*A/l

# Matriz de rigidez
# K = np.array([[k, -k, 0, 0], [-k, 2*k, -k, 0], [0, -k, 2*k, -k], [0, 0, -k, k]])
K = np.zeros([nnos, nnos])

for i in range(nnos):
    if (i == 0) or (i == nnos-1):
        K[i,i] = k
    else:
        K[i,i] = 2*k

    # Diagonal inferior
    if i > 0:
        K[i, i-1] = -k

    # Diagonal superior
    if i < nnos - 1:
        K[i, i+1] = -k

# print(K)


# Vetor de Forças
F = np.zeros([nnos])
F[nnos-1] = f
# print(F)


# Condições de contorno
dofs = [i for i in range(1, nnos)]
# Uma forma melhor seria utilizar dofs = list(range(1, nnos))
#dofs = [1,2, 3]

# Redução das matrizes para os DOFS, aplicação das CC
K_dof = K[np.ix_(dofs, dofs)]
F_dof = F[dofs]
# print(K_dof)
# print(F_dof)

# # Resolução do sistema
u_livres = np.linalg.solve(K_dof, F_dof)
# print(u_livres)

# Vetor completo de deslocamentos
u = np.zeros(nnos)
u[dofs] = u_livres
# print(u)

# Forças globais internas / reações
R = K @ u - F

# Cálculo da deformação em cada elemento
du = np.diff(u)
strain = du / l

N = E * A * strain

x_elem = np.linspace(0, L, nnos-1)

# plt.step(x_elem, N/1000, where='post')
# plt.xlabel('Comprimento [m]')
# plt.ylabel('Força Normal [kN]')
# plt.title('Diagrama de Força Normal')
# plt.grid()
# plt.show()
#######################################
x = np.linspace(0, L, nnos)

plt.plot(x, u*1000, marker='o')
plt.xlabel('Comprimento [m]')
plt.ylabel('Deslocamento [mm]')
plt.title('Diagrama de Deslocamento')
plt.grid()
plt.show()