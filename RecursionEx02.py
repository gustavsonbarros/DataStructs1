"""Escreva uma funcao recursiva que verifique se uma lista esta ordenada"""

def verificarOrdenacao(lista):
    if not lista:
        return True

    if len(lista) == 1:
        return True

    if lista[0] <= lista[1]:
        return verificarOrdenacao(lista[1:])

    else:
        return False

lista = [3, 1]
listaordem = verificarOrdenacao(lista)
print(listaordem)
