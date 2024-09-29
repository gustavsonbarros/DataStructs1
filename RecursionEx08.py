def verificarPalindromo(lista):
    if not lista:
        return True

    else:
        if lista[0] == lista[-1]:
            return verificarPalindromo(lista[1: -1])

    return False

lista = [1, 2, 3, 2, 1]
resultadoPalindromo = verificarPalindromo(lista)
print(resultadoPalindromo)