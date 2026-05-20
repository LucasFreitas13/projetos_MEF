import numpy as np

def resolver_sistema_linear(matriz_K, vetor_F, dofs_livres):
    """   
    Resolve o sistema linear K u = F aplicando condições de contorno
    via redução dos graus de liberdade livres.

    Parâmetros:
    ----------
    matriz_K : ndarray
        Matriz de rigidez global (NxN)
    vetor_F : ndarray
        Vetor de forças global (N)
    dofs_livres : list[int]
        Índices dos graus de liberdade livres

    Retorna:
    -------
    u : ndarray
        Vetor de deslocamentos global (N)
    """
    # Validações
    if matriz_K.shape[0] != matriz_K.shape[1]:
        raise ValueError("Matriz K deve ser quadrada")

    if len(vetor_F) != matriz_K.shape[0]:
        raise ValueError("Dimensões incompatíveis entre K e F")
    
    if len(dofs_livres) == 0:
        raise ValueError("Lista de DOFs livres está vazia")

    if min(dofs_livres) < 0 or max(dofs_livres) >= len(vetor_F):
        raise ValueError("DOFs livres fora do intervalo válido")
    
    # Definição do número de nós
    nnos = len(vetor_F)


    # Redução das matrizes para os DOFS, aplicação das CC
    K_dof = matriz_K[np.ix_(dofs_livres, dofs_livres)]
    F_dof = vetor_F[dofs_livres]

    # Resolução do sistema reduzido
    try:
        u_livres = np.linalg.solve(K_dof, F_dof)
    except np.linalg.LinAlgError:
        raise ValueError("Sistema linear não pode ser resolvido (matriz singular)")

    # Vetor completo de deslocamentos
    u = np.zeros(nnos)
    u[dofs_livres] = u_livres

    return u