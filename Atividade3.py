# Ordena a lista de tuplas pelo nome 
def ordenar_por_nome(lista_de_tuplas):

    lista_ordenada = sorted(lista_de_tuplas, key=lambda x: x[0])
    return lista_ordenada

#Resultado
lista_pessoas = [("Julia", 25), ("Bruna", 30), ("Carlos", 22), ("Ana", 28)]
lista_ordenada = ordenar_por_nome(lista_pessoas)
print(lista_ordenada)
