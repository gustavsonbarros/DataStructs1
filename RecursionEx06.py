#Crie uma funcao recursiva para gerar todas as permutacoes de uma lista

def permutacao(lista):
    if not lista:
        return [[]]

    resultado = []
    for i in range(len(lista)):
        atual = lista[i]
        resto = lista[:i] + lista[i + 1:]
        for perm in permutacao(resto):
            resultado.append([atual] + perm)

    return resultado

lista = [1, 2, 3]
gerarPerm = permutacao(lista)
print(gerarPerm)

