
import time
import random
from kruskal import kruskal

vertices = ["A", "B", "C", "D", "E", "F"]
aristas = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5),
    ("C", "D", 8), ("C", "E", 10), ("D", "E", 2), ("D", "F", 6),
    ("E", "F", 2)
]

print("=== KRUSKAL: ARBOL DE EXPANSION MINIMA ===")

arbol, total = kruskal(vertices, aristas)

for u, v, peso in arbol:
    print(f"{u} - {v} (peso {peso})")
print(f"Peso total: {total}")


def generar_grafo_conexo(cantidad):
    vertices = list(range(cantidad))
    aristas = []

    # Cadena que une todos los vertices, asi el grafo es conexo
    for i in range(cantidad - 1):
        aristas.append((i, i + 1, random.randint(1, 100)))

    # Aristas extra al azar
    for _ in range(cantidad * 3):
        a = random.randrange(cantidad)
        b = random.randrange(cantidad)
        if a != b:
            aristas.append((a, b, random.randint(1, 100)))

    return vertices, aristas


print("\n=== COMPARACION DE TIEMPOS ===")
print("Vertices | Aristas | Kruskal (ms) | Peso total")

random.seed(42)

for cantidad in [1000, 5000, 10000, 20000]:
    vertices_prueba, aristas_prueba = generar_grafo_conexo(cantidad)

    inicio = time.perf_counter()
    arbol_prueba, total_prueba = kruskal(vertices_prueba, aristas_prueba)
    tiempo = (time.perf_counter() - inicio) * 1000

    assert len(arbol_prueba) == cantidad - 1, "El arbol no tiene V - 1 aristas"

    print(f"{cantidad:8} | {len(aristas_prueba):7} | {tiempo:12.3f} | {total_prueba}")
