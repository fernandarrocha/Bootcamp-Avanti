def encontrar_maximo_e_minimo(lista):
    # Certifique-se de que a lista não está vazia
    if not lista:
        return None, None

    # Inicializa as variáveis de máximo e mínimo com o primeiro elemento da lista
    maximo = lista[0]
    minimo = lista[0]

    # Itera sobre os elementos da lista para encontrar o máximo e o mínimo
    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo

# Exemplo de uso:
lista_numeros = [10, 5, 8, 20, 3]
maximo, minimo = encontrar_maximo_e_minimo(lista_numeros)

print("Máximo:", maximo)
print("Mínimo:", minimo)
