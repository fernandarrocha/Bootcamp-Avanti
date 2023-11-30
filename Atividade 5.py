#Verifica se a lista ta vazia
def encontrar_maximo_e_minimo(lista):
    if not lista:
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    #Para encontrar o máximo e o mínimo
    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo

lista_numeros = [10, 5, 8, 20, 3]
maximo, minimo = encontrar_maximo_e_minimo(lista_numeros)

print("Máximo:", maximo)
print("Mínimo:", minimo)
