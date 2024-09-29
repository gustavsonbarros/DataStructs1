
"""
Crie uma funcao recursiva para inverter uma lista
"""

def inversao(lista):
    if not lista:   #caso base, define a condicao de parada, quando a condicao é atingida
        return []

    else:
        """Pegamos o ultimo elemento da lista e adicionamos a frente da lista
        depois chamamos a funcao novamente mas dessa vez passando a lista sem o ultimo elemento"""

        return [lista[-1]] + inversao(lista[:-1])


lista = [1, 3, 6, 9, 10]
listainvertida = inversao(lista)
print(listainvertida)
