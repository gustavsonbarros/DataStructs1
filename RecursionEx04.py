def contarElemento(lista, elemento):
    if not lista:
        return 0

    else:
        if lista[0] == elemento:
            return 1 + contarElemento(lista[1:], elemento)

        else:
            return contarElemento(lista[1:], elemento)

lista = [1, 1, 1, 2, 4, 5]
print(contarElemento(lista, 1))
