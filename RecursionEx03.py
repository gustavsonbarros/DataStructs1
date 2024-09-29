def maiorElemento(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        restoLista = maiorElemento(lista[1:])
        if lista[0] > restoLista:
            return lista[0]

        else:
            return restoLista

lista = [10, 2, 4, 5]
maior = maiorElemento(lista)
print(maior)