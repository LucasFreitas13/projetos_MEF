import numpy as np
import matplotlib.pyplot as plt

def calcular_reacoes(K, u, F):
    """
    Calcula o vetor de reações nodais do sistema.

    As reações são obtidas pela diferença entre as forças internas
    (K @ u) e as forças externas aplicadas (F).

    Parâmetros:
    ----------
    K : ndarray
        Matriz de rigidez global
    u : ndarray
        Vetor de deslocamentos nodais
    F : ndarray
        Vetor de forças externas aplicadas

    Retorna:
    -------
    R : ndarray
        Vetor de reações nodais
    """
    return K @ u - F


import numpy as np
import matplotlib.pyplot as plt

def plotar_resultados(u, L, E, A):
    """
    Plota os diagramas de deslocamento e força normal ao longo da barra.

    Parâmetros:
    ----------
    u : ndarray
        Vetor de deslocamentos nodais
    L : float
        Comprimento total da barra
    E : float
        Módulo de elasticidade
    A : float
        Área da seção transversal
    """

    nnos = len(u)

    # Comprimento de cada elemento
    l = L / (nnos - 1)

    # Cálculo das deformações
    du = np.diff(u)
    strain = du / l

    # Força normal em cada elemento
    N = E * A * strain

    # Coordenadas
    x_nos = np.linspace(0, L, nnos)
    x_elem = np.linspace(0, L, nnos - 1)

    # Plot 1 - Força Normal
    plt.figure()
    plt.step(x_elem, N / 1000, where='post')
    plt.xlabel('Comprimento [m]')
    plt.ylabel('Força Normal [kN]')
    plt.title('Diagrama de Força Normal')
    plt.grid()

    # Plot 2 - Deslocamento
    plt.figure()
    plt.plot(x_nos, u * 1000, marker='o')
    plt.xlabel('Comprimento [m]')
    plt.ylabel('Deslocamento [mm]')
    plt.title('Diagrama de Deslocamento')
    plt.grid()

    plt.show()