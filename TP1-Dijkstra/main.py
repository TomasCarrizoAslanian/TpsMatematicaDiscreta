
import time
import random
from dijkstra import dijkstra_array, dijkstra_heap

grafo = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("C", 2), ("D", 1)],
    "C": [("A", 1), ("B", 2), ("D", 5)],
    "D": [("B", 1), ("C", 5)]
}

print("=== DIJKSTRA: COMPARACION DE ALGORITMOS ===")

resultado_array = dijkstra_array(grafo, "A")
resultado_heap = dijkstra_heap(grafo, "A")

print("\nDistancias minimas desde A:")
for vertice in resultado_array:
    print(f"{vertice}: {resultado_array[vertice]}")

print("\n¿Ambos algoritmos dan el mismo resultado?")
print(resultado_array == resultado_heap)

def generar_grafo(cantidad):
    grafo = {i: [] for i in range(cantidad)}

    for i in range(cantidad - 1):
        peso = random.randint(1, 20)
        grafo[i].append((i + 1, peso))
        grafo[i + 1].append((i, peso))

    for _ in range(cantidad * 3):
        a = random.randrange(cantidad)
        b = random.randrange(cantidad)

        if a != b:
            peso = random.randint(1, 20)
            grafo[a].append((b, peso))
            grafo[b].append((a, peso))

    return grafo


print("\n=== COMPARACION DE TIEMPOS ===")
print("Vertices | Array (ms) | Priority Queue (ms)")

random.seed(42)

for cantidad in [100, 500, 1000, 2000]:
    grafo_prueba = generar_grafo(cantidad)

    inicio = time.perf_counter()
    dist_array = dijkstra_array(grafo_prueba, 0)
    tiempo_array = (time.perf_counter() - inicio) * 1000

    inicio = time.perf_counter()
    dist_heap = dijkstra_heap(grafo_prueba, 0)
    tiempo_heap = (time.perf_counter() - inicio) * 1000

    assert dist_array == dist_heap, "Los resultados no coinciden"

    print(f"{cantidad:8} | {tiempo_array:10.3f} | {tiempo_heap:19.3f}")
