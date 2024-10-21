# Trabajo Grafos

Este proyecto implementa el algoritmo de Dijkstra para calcular la ruta más corta en la red del Metro de Santiago. Permite buscar la mejor ruta según dos criterios: tiempo de viaje o número de transbordos.

### Características

- Algoritmo de Dijkstra: Calcula la ruta más corta en la red de metro.
- Dos modos de búsqueda:
	- Minimizar tiempo: Busca la ruta con el menor tiempo de viaje.
	- Minimizar transbordos: Encuentra la ruta con el menor número de transbordos, penalizando cada estación de transbordo.
- Simulación de red de metro: La red del Metro de Santiago se modela como un grafo, donde cada nodo representa una estación y los arcos ponderados representan el tiempo de viaje entre estaciones.

### Uso

1.  Al ejecutar el archivo Metodo Dijkstra Metro Santiago.py, se solicitarán tres entradas:
	- Estación de origen: El nombre de la estación de inicio.
	- Estación de destino: El nombre de la estación final.
	- Criterio de búsqueda: "tiempo" para la ruta más rápida o "transbordos" para minimizar la cantidad de transbordos.
2. El programa mostrará la ruta calculada, el tiempo estimado de viaje y el número de transbordos necesarios.

### Ejemplo De Uso

```python
Ingrese la estación de origen: Los Leones L1
Ingrese la estación de destino: Plaza de Maipú
Ingrese el criterio de búsqueda (tiempo/transbordos): tiempo

Ruta desde Los Leones L1 hasta Plaza de Maipú: ['Los Leones L1', 'Tobalaba L1', ..., 'Plaza de Maipú']
Tiempo estimado de viaje: 35 minutos
```




