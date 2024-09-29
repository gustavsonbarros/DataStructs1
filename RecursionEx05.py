def removerDuplicado(lista):
    if not lista:
        return []

    primeiro = lista[0]
    resto = lista[1:]

    if primeiro in resto:
        return removerDuplicado(resto)

    else:
        return [primeiro] + removerDuplicado(resto)

lista = [1, 1, 2, 2, 3, 4, 5]
listaremove = removerDuplicado(lista)
print(listaremove)