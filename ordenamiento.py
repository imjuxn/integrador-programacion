import time

def bubble_sort(lista):
    """Ordena la lista usando el algoritmo burbuja."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    """Ordena la lista usando el algoritmo de selección."""
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


# Entrada del usuario

entrada = input("Ingrese una lista de números separados por comas (ej: 5,2,9,1,4): ")
lista_usuario = [int(x.strip()) for x in entrada.split(',')]


# Ejecutar ambos algoritmos


# Burbuja
inicio_burbuja = time.time()
resultado_burbuja = bubble_sort(lista_usuario.copy())
fin_burbuja = time.time()

# Selección
inicio_seleccion = time.time()
resultado_seleccion = selection_sort(lista_usuario.copy())
fin_seleccion = time.time()


# Mostrar resultados

print("\n--- Resultados del ordenamiento ---")
print(f"Original:         {lista_usuario}")
print(f"Burbuja:          {resultado_burbuja} (Tiempo: {fin_burbuja - inicio_burbuja:.6f} seg)")
print(f"Selección:        {resultado_seleccion} (Tiempo: {fin_seleccion - inicio_seleccion:.6f} seg)")


# Comparación con listas grandes

print("\n--- Comparación de rendimiento con listas aleatorias ---")

# Burbuja pequeña
inicio = time.time()
fin = time.time()
print(f"Burbuja - pequeña:   {fin - inicio:.6f} seg")

# Burbuja grande
inicio = time.time()
fin = time.time()
print(f"Burbuja - grande:    {fin - inicio:.6f} seg")

# Selección pequeña
inicio = time.time()
fin = time.time()
print(f"Selección - pequeña: {fin - inicio:.6f} seg")

# Selección grande
inicio = time.time()
fin = time.time()
print(f"Selección - grande:  {fin - inicio:.6f} seg")

