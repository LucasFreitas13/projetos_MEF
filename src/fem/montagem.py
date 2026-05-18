import numpy as np

def montar_matriz_rigidez_barra_1D(nnos, E, A, L): 
    """
    Monta a matriz de rigidez global para uma barra 1D
    usando elementos finitos lineares.

    Parâmetros:
    ----------
    nnos : int
        Número de nós
    E : float
        Módulo de elasticidade
    A : float
        Área da seção transversal
    L : float
        Comprimento total da barra

    Retorna:
    -------
    K : ndarray
        Matriz de rigidez global (nnos x nnos)
    """

    l = L / (nnos-1) # Comprimento de cada elemento
    
    k = (E * A) / l # Rigidezde cada elemento

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
        
    return K

def montar_vetor_forcas(nnos, forcas_nodais):
    """
    Monta o vetor de forças.

    Parâmetros:
    ----------
    nnos : int
        Número de nós
    forcas_nodais : float
        Carga 

    Retorna:
    -------
    F : ndarray
        Vetor de forças (nnos x 1)   
    """
    F = np.zeros(nnos)

    for no, valor in forcas_nodais.items():
        F[no] = valor

    return F