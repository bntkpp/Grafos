def dijkstra_metro(grafo, origen, destino, criterio):
   
    # Inicializacion de distancias y predecesores
    dist = {nodo: float('inf') for nodo in grafo}  # Distancia inicial desde el origen
    dist[origen] = 0 
    prev = {nodo: None for nodo in grafo} 
    transbordos = {nodo: 0 for nodo in grafo}  # Contador de transbordos
    visitados = set() # Nodos visitados

    while len(visitados) < len(grafo):
        # Encontrar el nodo con la distancia mas pequeña que aun no ha sido visitado
        estacion = min((nodo for nodo in grafo if nodo not in visitados), key=lambda nodo: dist[nodo]) 

        # Si llegamos al destino, terminamos
        if estacion == destino:
            break

        visitados.add(estacion) # Marcar como visitado

        # Relajar las aristas adyacentes
        for vecino, peso in grafo[estacion].items():
            if vecino not in visitados: # Si no ha sido visitado
                if criterio == 'tiempo':
                    new_dist = dist[estacion] + peso  # Minimizar tiempo

                elif criterio == 'transbordos':
                    new_dist = dist[estacion] + 1  # Minimizar transbordos

                # Actualizamos si encontramos una distancia mejor
                if new_dist < dist[vecino]: 
                    dist[vecino] = new_dist 
                    prev[vecino] = estacion
                    if criterio == 'transbordos':
                        transbordos[vecino] = transbordos[estacion] + 1

    # Reconstruccion del camino
    camino = []
    nodo_actual = destino
    while nodo_actual is not None: # Mientras no lleguemos al origen
        camino.insert(0, nodo_actual) # Insertar al principio
        nodo_actual = prev[nodo_actual] # Mover al predecesor

    return dist, camino

# Grafo del Metro de Santiago
grafo = {
    # Linea 1 (Roja)
    'San Pablo L1': {'San Pablo L5': 5, 'Neptuno': 2},
    'Neptuno': {'Pajaritos': 2, 'San Pablo L1': 2},
    'Pajaritos': {'Las Rejas': 2, 'Neptuno': 2},
    'Las Rejas': {'Ecuador': 2, 'Pajaritos': 2},
    'Ecuador': {'San Alberto Hurtado': 2, 'Las Rejas': 2},
    'San Alberto Hurtado': {'Universidad de Santiago': 2, 'Ecuador': 2},
    'Universidad de Santiago': {'Estacion Central': 2, 'San Alberto Hurtado': 2},
    'Estacion Central': {'Union Latinoamericana': 2, 'Universidad de Santiago': 2},
    'Union Latinoamericana': {'Republica': 2, 'Estacion Central': 2},
    'Republica': {'Los Heroes L1': 2, 'Union Latinoamericana': 2},
    'Los Heroes L1': {'La Moneda': 2, 'Republica': 2, 'Los Heroes L2': 5},
    'La Moneda': {'Universidad de Chile L1': 2, 'Los Heroes L1': 2},
    'Universidad de Chile L1': {'Santa Lucia': 2, 'La Moneda': 2, 'Universidad de Chile L3': 5},
    'Santa Lucia': {'Universidad Catolica': 2, 'Universidad de Chile L1': 2},
    'Universidad Catolica': {'Baquedano L1': 2, 'Santa Lucia': 2},
    'Baquedano L1': {'Salvador': 2, 'Universidad Catolica': 2, 'Baquedano L5': 5},
    'Salvador': {'Manuel Montt': 2, 'Baquedano L1': 2},
    'Manuel Montt': {'Pedro de Valdivia': 2, 'Salvador': 2},
    'Pedro de Valdivia': {'Los Leones L1': 2, 'Manuel Montt': 2},
    'Los Leones L1': {'Tobalaba L1': 2, 'Pedro de Valdivia': 2, 'Los Leones L6': 5},
    'Tobalaba L1': {'El Golf': 2,'Cristobal Colon': 2, 'Los Leones L1': 2, 'Tobalaba L4': 5},
    'El Golf': {'Alcantara': 2, 'Tobalaba L1': 2},
    'Alcantara':{'Escuela Militar': 2, 'El Golf': 2},
    'Escuela Militar': {'Manquehue': 3, 'Alcantara': 2},
    'Manquehue': {'Hernando de Magallanes': 2, 'Escuela Militar': 2},
    'Hernando de Magallanes': {'Los Dominicos': 3, 'Manquehue': 2},
    'Los Dominicos': {'Hernando de Magallanes': 3},

    # Linea 2 (Amarilla)
    'Hospital El Pino': {'Copa Lo Martinez': 3},
    'Copa Lo Martinez': {'Hospital El Pino': 3, 'Observatorio': 2},
    'Observatorio': {'Copa Lo Martinez': 2, 'El Bosque': 3},
    'El Bosque': {'Observatorio': 3, 'La Cisterna L2': 2},
    'La Cisterna L2': {'El Bosque': 2, 'El Parron': 3, 'La Cisterna L4A': 5},
    'El Parron': {'La Cisterna L2': 3, 'Lo Ovalle': 2},
    'Lo Ovalle': {'El Parron': 2, 'Ciudad del Niño': 2},
    'Ciudad del Niño': {'Lo Ovalle': 2, 'Departamental': 2},
    'Departamental': {'Ciudad del Niño': 2, 'Lo Vial': 2},
    'Lo Vial': {'Departamental': 2, 'San Miguel': 2},
    'San Miguel': {'Lo Vial': 2, 'El Llano': 2},
    'El Llano': {'San Miguel': 2, 'Franklin L2': 2},
    'Franklin L2': {'El Llano': 2, 'Rondizzoni': 2, 'Franklin L6': 5},
    'Rondizzoni': {'Franklin L2': 2, 'Parque O\'Higgins': 2},
    'Parque O\'Higgins': {'Rondizzoni': 2, 'Toesca': 2},
    'Toesca': {'Parque O\'Higgins': 2, 'Los Heroes L2': 2},
    'Los Heroes L2': {'Santa Ana L2': 2, 'Toesca': 2, 'Los Heroes L1': 5},
    'Santa Ana L2': {'Los Heroes L2': 2, 'Puente Cal y Canto L2': 3, 'Santa Ana L5': 5},
    'Puente Cal y Canto L2': {'Santa Ana L2': 3, 'Patronato': 2, 'Puente Cal y Canto L3': 5},
    'Patronato': {'Puente Cal y Canto L2': 2, 'Cerro Blanco': 2},
    'Cerro Blanco': {'Patronato': 2, 'Cementerios': 2},
    'Cementerios': {'Cerro Blanco': 2, 'Einstein': 2},
    'Einstein': {'Cementerios': 2, 'Dorsal': 2},
    'Dorsal': {'Einstein': 2, 'Zapadores': 2},
    'Zapadores': {'Dorsal': 2, 'Vespucio Norte': 3},
    'Vespucio Norte': {'Zapadores': 3},

    # Linea 3 (Cafe)
    'Plaza Quilicura': {'Lo Cruzat': 2},
    'Lo Cruzat': {'Plaza Quilicura': 2, 'Ferrocarril': 3},
    'Ferrocarril': {'Lo Cruzat': 3, 'Los Libertadores': 3},
    'Los Libertadores': {'Ferrocarril': 3, 'Cardenal Caro': 2},
    'Cardenal Caro': {'Los Libertadores': 2, 'Vivaceta': 3},
    'Vivaceta': {'Cardenal Caro': 3, 'Conchali': 3},
    'Conchali': {'Vivaceta': 3, 'Plaza Chacabuco': 3},
    'Plaza Chacabuco': {'Conchali': 3, 'Hospitales': 3},
    'Hospitales': {'Plaza Chacabuco': 3, 'Puente Cal y Canto L3': 3},
    'Puente Cal y Canto L3': {'Puente Cal y Canto L2': 5, 'Hospitales': 3, 'Plaza de Armas L3': 2},
    'Plaza de Armas L3': {'Puente Cal y Canto L3': 3, 'Universidad de Chile L3': 2, 'Plaza de Armas L5': 5},
    'Universidad de Chile L3': {'Plaza de Armas L3': 2, 'Parque Almagro': 2, 'Universidad de Chile L1': 5},
    'Parque Almagro': {'Universidad de Chile L3': 2, 'Matta': 3},
    'Matta': {'Parque Almagro': 3, 'Irarrazaval L3': 3},
    'Irarrazaval L3': {'Matta': 3, 'Monseñor Eyzaguirre': 3, 'Irarrazaval L5': 5},
    'Monseñor Eyzaguirre': {'Irarrazaval L3': 3, 'Ñuñoa L3': 2},
    'Ñuñoa L3': {'Monseñor Eyzaguirre': 2, 'Chile España': 2, 'Ñuñoa L6': 5},
    'Chile España': {'Ñuñoa L3': 2, 'Villa Frei': 3},
    'Villa Frei': {'Chile España': 3, 'Plaza Egaña L3': 2},
    'Plaza Egaña L3': {'Villa Frei': 2, 'Fernando Castillo Velasco': 3, 'Plaza Egaña L4': 5},
    'Fernando Castillo Velasco': {'Plaza Egaña L3': 3},

    # Linea 4 (Azul)
    'Tobalaba L4': {'Tobalaba L1': 5, 'Cristobal Colon': 2},
    'Cristobal Colon': {'Tobalaba L4': 2, 'Francisco Bilbao': 2},
    'Francisco Bilbao': {'Cristobal Colon': 2, 'Principe de Gales': 3},
    'Principe de Gales': {'Francisco Bilbao': 3, 'Simon Bolivar': 2},
    'Simon Bolivar': {'Principe de Gales': 2, 'Plaza Egaña L4': 2},
    'Plaza Egaña L4': {'Plaza Egaña L3': 5, 'Simon Bolivar': 2, 'Los Orientales': 2},
    'Los Orientales': {'Plaza Egaña L4': 2, 'Grecia': 2},
    'Grecia': {'Los Orientales': 2, 'Los Presidentes': 2},
    'Los Presidentes': {'Grecia': 2, 'Quilin': 2},
    'Quilin': {'Los Presidentes': 2, 'Las Torres': 2},
    'Las Torres': {'Quilin': 2, 'Macul': 2},
    'Macul': {'Las Torres': 2, 'Vicuña Mackenna L4': 3},
    'Vicuña Mackenna L4': {'Macul': 3, 'Vicente Valdes L4': 2, 'Vicuña Mackenna L4A': 5},
    'Vicente Valdes L4': {'Vicente Valdes L5': 5,'Vicuña Mackenna L4': 2, 'Rojas Magallanes': 2},
    'Rojas Magallanes': {'Vicente Valdes L4': 2, 'Trinidad': 2},
    'Trinidad': {'Rojas Magallanes': 2, 'San Jose de la Estrella': 2},
    'San Jose de la Estrella': {'Trinidad': 2, 'Los Quillayes': 2},
    'Los Quillayes': {'San Jose de la Estrella': 2, 'Elisa Correa': 2},
    'Elisa Correa': {'Los Quillayes': 2, 'Hospital Sotero del Rio': 2},
    'Hospital Sotero del Rio': {'Elisa Correa': 2, 'Protectora de la Infancia': 2},
    'Protectora de la Infancia': {'Hospital Sotero del Rio': 2, 'Las Mercedes': 2},
    'Las Mercedes': {'Protectora de la Infancia': 2, 'Plaza de Puente Alto': 2},
    'Plaza de Puente Alto': {'Las Mercedes': 2},

    # Linea 4A (Azul Claro)
    'Vicuña Mackenna L4A': {'Vicuña Mackenna L4': 5, 'Santa Julia': 4},
    'Santa Julia': {'La Granja': 2, 'Vicuña Mackenna L4A': 4}, 
    'La Granja': {'Santa Rosa': 4, 'Santa Julia': 2},
    'Santa Rosa': {'San Ramon': 2, 'La Granja': 4},
    'San Ramon': {'Santa Rosa': 2, 'La Cisterna L4A': 5},
    'La Cisterna L4A': {'La Cisterna L2': 5, 'San Ramon': 4},

    # Linea 5 (Verde)
    'Plaza de Maipu': {'Santiago Bueras': 3},
    'Santiago Bueras': {'Plaza de Maipu': 3, 'Del Sol': 2},
    'Del Sol': {'Santiago Bueras': 2, 'Monte Tabor': 2},
    'Monte Tabor': {'Del Sol': 2, 'Las Parcelas': 2},
    'Las Parcelas': {'Monte Tabor': 2, 'Laguna Sur': 3},
    'Laguna Sur': {'Las Parcelas': 3, 'Barrancas': 2},
    'Barrancas': {'Laguna Sur': 2, 'Pudahuel': 2},
    'Pudahuel': {'Barrancas': 2, 'San Pablo L5': 2},
    'San Pablo L5': {'San Pablo L1': 5, 'Lo Prado': 2, 'Pudahuel': 2},
    'Lo Prado': {'San Pablo L5': 2, 'Blanqueado': 2}, 
    'Blanqueado': {'Lo Prado': 2, 'Gruta de Lourdes': 2}, 
    'Gruta de Lourdes': {'Blanqueado': 2, 'Quinta Normal': 2},
    'Quinta Normal': {'Gruta de Lourdes': 2, 'Cumming': 2},
    'Cumming': {'Quinta Normal': 2, 'Santa Ana L5': 2},
    'Santa Ana L5': {'Cumming': 2, 'Plaza de Armas L5': 2, 'Santa Ana L2': 5},
    'Plaza de Armas L5': {'Bellas Artes': 2, 'Santa Ana L5': 2, 'Plaza de Armas L3': 5},
    'Bellas Artes': {'Plaza de Armas L5': 2, 'Baquedano L5': 2},
    'Baquedano L5': {'Bellas Artes': 2, 'Parque Bustamante': 2, 'Baquedano L1': 5},
    'Parque Bustamante': {'Santa Isabel': 2, 'Baquedano L5': 2},
    'Santa Isabel': {'Parque Bustamante': 2,'Irarrazaval L5': 2},
    'Irarrazaval L5': {'Irarrazaval L3': 5, 'Ñuble L5': 3,  'Santa Isabel': 2},
    'Ñuble L5': {'Irarrazaval L5': 3, 'Rodrigo de Araya': 2, 'Ñuble L6': 5},
    'Rodrigo de Araya': {'Ñuble L5': 2, 'Carlos Valdovinos': 2},
    'Carlos Valdovinos': {'Rodrigo de Araya': 2, 'Camino Agricola': 2},
    'Camino Agricola': {'Carlos Valdovinos': 2, 'San Joaquin': 2},
    'San Joaquin': {'Camino Agricola': 2, 'Pedrero': 2},
    'Pedrero': {'San Joaquin': 2, 'Mirador': 2},
    'Mirador': {'Pedrero': 2, 'Bellavista de La Florida': 2},
    'Bellavista de La Florida': {'Mirador': 2, 'Vicente Valdes L5': 2},
    'Vicente Valdes L5': {'Vicente Valdes L4': 5, 'Bellavista de La Florida': 2},

    # Linea 6 (Morada)
    'Cerrillos': {'Lo Valledor': 3},
    'Lo Valledor': {'Cerrillos': 3, 'Presidente Pedro Aguirre Cerda': 6},
    'Presidente Pedro Aguirre Cerda': {'Lo Valledor': 6,'Franklin L6': 3},
    'Franklin L6': {'Franklin L2': 5, 'Presidente Pedro Aguirre Cerda': 3, 'Bio Bio': 2},
    'Bio Bio': {'Franklin L6': 2, 'Ñuble L6': 4},
    'Ñuble L6': {'Ñuble L5': 5, 'Estadio Nacional': 4, 'Bio Bio': 4},
    'Estadio Nacional': {'Ñuble L6': 4, 'Ñuñoa L6': 2},
    'Ñuñoa L6': {'Ñuñoa L3': 5, 'Estadio Nacional': 2, 'Ines de Suarez': 3},
    'Ines de Suarez': {'Ñuñoa L6': 4, 'Los Leones L6': 5},
    'Los Leones L6': {'Ines de Suarez': 5, 'Los Leones L1': 5},
}

# Ejemplo de uso
origen = input("Ingrese la estacion de origen: ")
destino = input("Ingrese la estacion de destino: ")
criterio = input("Ingrese el criterio de busqueda (tiempo/transbordos): ")

# Ejecutar el algoritmo de Dijkstra
distancias, camino = dijkstra_metro(grafo, origen, destino, criterio)

# Mostrar resultados
distancia_total = distancias[destino]
print(f"Ruta desde {origen} hasta {destino}: {camino}")
if criterio == 'tiempo':
    print(f"Tiempo estimado de viaje: {distancia_total} minutos")
elif criterio == 'transbordos':
    print(f"Numero de transbordos: {distancia_total}")


