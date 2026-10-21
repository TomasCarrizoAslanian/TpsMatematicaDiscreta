# TP2 - Kruskal con Union-Find

Para este TP implemente el algoritmo de Kruskal en Python para encontrar el arbol de expansion minima (AEM) de un grafo no dirigido y ponderado.

- **kruskal.py:** la clase `UnionFind` (compresion de caminos y union por rango) y la funcion `kruskal`.
- **main.py:** ejecuta Kruskal sobre un grafo de ejemplo y mide los tiempos con grafos de distintos tamaños.

## Idea del algoritmo

1. Ordenar las aristas de menor a mayor peso.
2. Recorrerlas y agregar cada una al arbol solo si une dos componentes distintas (si no, formaria un ciclo).
3. Terminar cuando el arbol tiene V - 1 aristas.

Para saber si dos vertices ya estan en la misma componente se usa **Union-Find**:

- `find(x)`: devuelve el representante del conjunto de x. Con compresion de caminos, cada nodo recorrido queda apuntando directo a la raiz.
- `union(a, b)`: une los dos conjuntos colgando el arbol de menor rango del de mayor rango. Si ya estaban juntos, devuelve `False`.

## Complejidad

- Ordenar las aristas: O(E log E) = O(E log V), porque E <= V².
- E operaciones de Union-Find: O(E · α(V)), con α la inversa de Ackermann (en la practica, menor o igual a 4).
- **Total: O(E log V)**, dominado por el ordenamiento.

## Ejemplo

Con el grafo de `main.py`, el AEM tiene estas aristas:

```
B - C (peso 1)
A - C (peso 2)
D - E (peso 2)
E - F (peso 2)
B - D (peso 5)
Peso total: 12
```

Se descartan A-B (4), D-F (6), C-D (8) y C-E (10) porque formarian ciclo.

## Comparacion de tiempos

Grafos conexos al azar, con una cadena que une todos los vertices mas 3V aristas extra. Pesos entre 1 y 100, semilla 42. Los tiempos son de una sola corrida, asi que pueden variar un poco entre ejecuciones.

| Vertices | Aristas | Kruskal (ms) |
|---|---|---|
| 1.000 | 3.996 | 6,912 |
| 5.000 | 19.995 | 23,088 |
| 10.000 | 39.996 | 37,060 |
| 20.000 | 79.993 | 91,409 |

Al duplicar V y E, el tiempo crece algo mas del doble, lo que es consistente con O(E log E): el ordenamiento domina el costo.

## Ejecucion

Para correr el ejemplo y la comparacion:

```bash
python main.py
```

No hace falta instalar ninguna libreria externa.
