
# Kruskal: arbol de expansion minima (AEM) de un grafo no dirigido y ponderado.
# Se ordenan las aristas de menor a mayor peso y se agregan al arbol
# solo si no forman ciclo. Para detectar ciclos se usa Union-Find.


class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}

    # Compresion de caminos: cada nodo queda apuntando directo a la raiz
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    # Union por rango: el arbol mas bajo se cuelga del mas alto
    # Devuelve False si a y b ya estaban en el mismo conjunto (habria ciclo)
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.rango[ra] < self.rango[rb]:
            ra, rb = rb, ra
        self.padre[rb] = ra
        if self.rango[ra] == self.rango[rb]:
            self.rango[ra] += 1
        return True


def kruskal(vertices, aristas):
    uf = UnionFind(vertices)
    arbol = []
    total = 0

    # Ordenamos por peso: O(E log E)
    for u, v, peso in sorted(aristas, key=lambda arista: arista[2]):
        if uf.union(u, v):
            arbol.append((u, v, peso))
            total += peso
            # Con V - 1 aristas el arbol ya esta completo
            if len(arbol) == len(vertices) - 1:
                break

    return arbol, total
