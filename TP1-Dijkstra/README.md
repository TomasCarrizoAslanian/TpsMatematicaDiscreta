# TP1 - Dijkstra con Priority Queue

Para este TP implemente dos versiones del algoritmo de Dijkstra en Python:

- **dijkstra_array:** busca el vertice con menor distancia recorriendo los vertices no visitados.
- **dijkstra_heap:** utiliza una cola de prioridad con `heapq` para hacer esa busqueda mas eficiente.

En `dijkstra.py` estan las dos implementaciones y en `main.py` las ejecuto con los mismos grafos para comparar resultados y tiempos.

## Como funciona el algoritmo

Dijkstra busca las distancias minimas desde un vertice de origen hacia todos los demas, en un grafo con pesos no negativos.

Para hacerlo, primero guarda la distancia de cada vertice como infinito, excepto la del origen que empieza en 0.

Despues va seleccionando el vertice con menor distancia conocida y revisa sus vecinos. Si encuentra un camino mas corto hacia alguno, actualiza su distancia. A esto se lo llama **relajacion de aristas**.

### ¿Que cambia con la Priority Queue?

En la version tradicional (`dijkstra_array`), cada vez que necesitamos el siguiente vertice hay que recorrer todos los que todavia no fueron visitados para encontrar el de menor distancia.

En cambio, en `dijkstra_heap` usamos `heapq`, que implementa una cola de prioridad mediante un heap de minimos.

Las operaciones principales son:

- `heappush`: agrega un vertice con su distancia a la cola.
- `heappop`: extrae el elemento con menor distancia.

Estas operaciones cuestan O(log n), siendo n la cantidad de elementos en la cola, en lugar de tener que recorrer todos los vertices para buscar el minimo.

### ¿Por que se optimiza?

La diferencia esta en como seleccionamos el siguiente vertice, no en el calculo de las distancias.

Con el array, buscar el minimo cuesta O(V) y se repite hasta V veces, dando O(V²).

Con el heap, las inserciones y extracciones son logaritmicas, por lo que la complejidad total pasa a O((V + E) log V).

Ademas, cuando encontramos una distancia mejor, agregamos una nueva entrada a la cola. Si despues aparece una entrada vieja con una distancia mayor a la que ya tenemos guardada, la ignoramos con `continue`.

Esto permite actualizar las prioridades sin tener que modificar elementos que ya estan dentro del heap.

Por eso, en grafos dispersos, donde E es proporcional a V, pasamos de O(V²) a O(V log V).

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

## Comparacion con grafos densos

Tambien probe los algoritmos con grafos densos, donde todos los vertices estan conectados entre si.

En este caso, el array tiene complejidad O(V²), mientras que la version con priority queue tiene una cota de O(V² log V).

Por eso, usar una cola de prioridad no siempre mejora la complejidad. La mejora es especialmente importante en grafos dispersos.

### Resultados con grafos densos

| Vertices | Array (ms) | Priority Queue (ms) |
|---|---|---|
| 100 | 2.074 | 1.190 |
| 200 | 6.496 | 3.202 |
| 400 | 25.476 | 20.922 |
| 800 | 125.270 | 70.068 |

En estas pruebas la priority queue tambien fue mas rapida, aunque la diferencia fue menor que en los grafos dispersos.

Esto muestra que el rendimiento depende tambien de la cantidad de aristas y no solamente de los vertices. Los tiempos pueden variar entre ejecuciones.

## Ejecucion

Para correr la comparacion:

```bash
python main.py
```

No hace falta instalar ninguna libreria externa.
