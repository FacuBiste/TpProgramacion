import random
import time

# algoritmos de ordenamiento
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# algoritmos de busqueda
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# lista de prueba
numeros = [random.randint(0, 100) for _ in range(1000)]
print(numeros)

# medicon de tiempos
inicio = time.time()
bubble_sort(numeros.copy())
fin = time.time()
print(f"Bubble Sort: {fin - inicio:.6f} segundos")

inicio = time.time()
quick_sort(numeros.copy())
fin = time.time()
print(f"Quick Sort: {fin - inicio:.6f} segundos")

# busqueda
ordenada = sorted(numeros)
print("Lista ordenada:", ordenada)

print("Búsqueda lineal de 7:", busqueda_lineal(numeros, 7))
print("Búsqueda binaria de 4:", busqueda_binaria(ordenada, 4))
