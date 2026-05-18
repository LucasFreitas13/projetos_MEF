from src.fem.montagem import montar_vetor_forcas

# Número de nós
nnos = 4

# Definição das forças
forcas = {
    3: 1000,   # força no último nó
    1: -500    # força no nó 1
}

F = montar_vetor_forcas(nnos, forcas)

print(F)