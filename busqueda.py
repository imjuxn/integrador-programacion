import time


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


# Ingreso de datos
entrada = input("Ingrese una lista de números separados por comas (ej: 5,2,9,1,4): ")
lista = [int(x.strip()) for x in entrada.split(',')]

objetivo = int(input("Ingrese el número que desea buscar: "))

# Búsqueda Lineal
indice_lineal = busqueda_lineal(lista, objetivo)
if indice_lineal != -1:
    print(f"[Lineal] El número {objetivo} se encuentra en la posición {indice_lineal}")
else:
    print(f"[Lineal] El número {objetivo} no se encuentra en la lista.")


# Búsqueda Binaria 
lista_ordenada = sorted(lista)
indice_binaria = busqueda_binaria(lista_ordenada, objetivo)
if indice_binaria != -1:
    print(f"[Binaria] El número {objetivo} se encuentra en la posición {indice_binaria} (en la lista ordenada)")
else:
    print(f"[Binaria] El número {objetivo} no se encuentra en la lista ordenada.")

# Medir tiempo de búsqueda lineal
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(lista, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal

lista_ordenada = sorted(lista)  # Lista ordenada para búsqueda binaria
# Medir tiempo de búsqueda binaria
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(lista_ordenada, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

# Resultados
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")

print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.6f} segundos")

