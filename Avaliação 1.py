
#Verifica se o número é primo

def is_prime(num):  
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

#Recebendo lista de números

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_primos = filter_primes(lista_numeros)
print(lista_primos)
