# TP1 - Dijkstra con Priority Queue

Para este TP implemente dos versiones del algoritmo de Dijkstra en Python:

- **dijkstra_array:** busca el vertice con menor distancia recorriendo los vertices no visitados.
- **dijkstra_heap:** utiliza una cola de prioridad con `heapq` para hacer esa busqueda mas eficiente.

En `dijkstra.py` estan las dos implementaciones y en `main.py` las ejecuto con los mismos grafos para comparar resultados y tiempos.

## Comparacion de tiempos

Probe las dos versiones con grafos de distintos tamaños. En todos los casos devolvieron las mismas distancias minimas.

| Vertices | Array (ms) | Priority Queue (ms) |
|---|---|---|
| 100 | 1.133 | 0.201 |
| 500 | 29.505 | 1.530 |
| 1000 | 91.170 | 3.176 |
| 2000 | 561.159 | 13.197 |

## ¿Mejora la complejidad? ¿Cuanto?

Si, mejora principalmente en grafos dispersos.

- **Con array:** O(V² + E)
- **Con priority queue:** O((V + E) log V)

Donde V es la cantidad de vertices y E la cantidad de aristas.

La mejora se debe a que con un array hay que recorrer los vertices para encontrar el de menor distancia, mientras que con un heap se puede extraer el minimo de forma mas eficiente.

En grafos dispersos, la complejidad pasa de **O(V²) a O(V log V)**.

En las pruebas, con 2000 vertices, la version con priority queue fue aproximadamente **42 veces mas rapida** que la version con array.

## Ejecucion

Para correr la comparacion:

```bash
python main.py
```

No hace falta instalar ninguna libreria externa.
