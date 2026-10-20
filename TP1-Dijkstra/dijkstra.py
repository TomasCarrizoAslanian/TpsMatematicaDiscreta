
import heapq
# Version tradicional: seleccion del minimo mediante array
def dijkstra_array(grafo, origen):
    distancias = {v: float("inf") for v in grafo}
    distancias[origen] = 0
    visitados = set()

    while len(visitados) < len(grafo):
        actual = None

        # Buscamos el vertice no visitado con menor distancia
        for vertice in grafo:
            if vertice not in visitados:
                if actual is None or distancias[vertice] < distancias[actual]:
                    actual = vertice

        if actual is None or distancias[actual] == float("inf"):
            break

        visitados.add(actual)

        for vecino, peso in grafo[actual]:
            nueva_distancia = distancias[actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia

    return distancias


# Version optimizada: seleccion mediante cola de prioridad
def dijkstra_heap(grafo, origen):
    distancias = {v: float("inf") for v in grafo}
    distancias[origen] = 0

    cola = [(0, origen)]

    while cola:
        distancia, actual = heapq.heappop(cola)

        # Ignoramos entradas que ya fueron mejoradas
        if distancia > distancias[actual]:
            continue

        for vecino, peso in grafo[actual]:
            nueva_distancia = distancia + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias
