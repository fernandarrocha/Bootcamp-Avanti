#Criando conjunto de lista
def unique_elements(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)

    # Calcula a diferença entre cada lista
    result_set = set1.symmetric_difference(set2)

    # Converte o resultado de volta para uma lista
    result_list = list(result_set)

    return result_list


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = unique_elements(lista1, lista2)
print(resultado)
