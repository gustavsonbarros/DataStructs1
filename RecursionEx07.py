#Funcao recursiva para somar elementos pares dentro de uma lista

def somarElementoPares(lista):
    if not lista:
        return 0

    primeiro = lista[0]
    resto = lista[1:]

    if primeiro % 2 == 0:
        return primeiro + somarElementoPares(resto)
    else:
        return somarElementoPares(resto)

lista = [1, 2, 3, 4, 5, 6]
resultadodaSoma = somarElementoPares(lista)
print(resultadodaSoma)