"""14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""

from Graph import Graph

g = Graph(is_directed=False)

ambientes = [
    "cocina", "comedor", "cochera", "quincho", "bano1", "bano2",
    "habitacion1", "habitacion2", "sala_estar", "terraza", "patio"
]

for amb in ambientes:
    g.insert_vertex(amb)

#Carga de aristas

# Cocina
g.insert_edge("cocina", "comedor", 4)
g.insert_edge("cocina", "bano1", 6)
g.insert_edge("cocina", "habitacion1", 8)

# Comedor (5 conexiones)
g.insert_edge("comedor", "cocina", 4)
g.insert_edge("comedor", "sala_estar", 7)
g.insert_edge("comedor", "terraza", 12)
g.insert_edge("comedor", "bano2", 6)
g.insert_edge("comedor", "habitacion2", 10)

# Cochera
g.insert_edge("cochera", "quincho", 9)
g.insert_edge("cochera", "patio", 11)
g.insert_edge("cochera", "habitacion1", 15)

# Quincho (5 conexiones)
g.insert_edge("quincho", "cochera", 9)
g.insert_edge("quincho", "patio", 5)
g.insert_edge("quincho", "terraza", 14)
g.insert_edge("quincho", "bano2", 13)
g.insert_edge("quincho", "sala_estar", 18)

# Baño 1
g.insert_edge("bano1", "cocina", 6)
g.insert_edge("bano1", "habitacion1", 3)
g.insert_edge("bano1", "terraza", 9)

# Baño 2
g.insert_edge("bano2", "comedor", 6)
g.insert_edge("bano2", "quincho", 13)
g.insert_edge("bano2", "habitacion2", 4)

# Habitacion 1
g.insert_edge("habitacion1", "bano1", 3)
g.insert_edge("habitacion1", "cocina", 8)
g.insert_edge("habitacion1", "cochera", 15)

# Habitacion 2
g.insert_edge("habitacion2", "bano2", 4)
g.insert_edge("habitacion2", "comedor", 10)
g.insert_edge("habitacion2", "terraza", 16)

# Sala de estar
g.insert_edge("sala_estar", "comedor", 7)
g.insert_edge("sala_estar", "quincho", 18)
g.insert_edge("sala_estar", "terraza", 5)

# Terraza
g.insert_edge("terraza", "comedor", 12)
g.insert_edge("terraza", "sala_estar", 5)
g.insert_edge("terraza", "habitacion2", 16)

# Patio
g.insert_edge("patio", "quincho", 5)
g.insert_edge("patio", "cochera", 11)
g.insert_edge("patio", "terraza", 20)




# Funcion auxliar para reconstruie el camino (DIJKSTRA)


def reconstruir_camino(stack, origen, destino):
    camino = []
    peso_total = None
    actual = destino
    while stack.size() > 0:
        nodo = stack.pop()
        nombre, costo, predecesor = nodo
        if nombre == actual:
            if peso_total is None:
                peso_total = costo
            camino.append(nombre)
            actual = predecesor
    if len(camino) == 0:
        return None, None
    camino.reverse()
    return camino, peso_total



# C Arbol de expansion minima


def mst_total():
    resultado = g.kruskal("cocina")

    print("\nArbol de expansion minima (salida cruda del metodo):")
    print(resultado)

    # formato: "n1-n2-peso;n3-n4-peso;..."
    partes = resultado.split(";")
    total = 0
    for p in partes:
        if "-" in p:
            _, _, w = p.split("-")
            total += int(w)

    print(f"\nMetros totales necesarios para conectar todo: {total} metros")




# D  Camino mas corto de la habitacion1 hacia SALA ESTAR


def camino_h1_sala():
    stack = g.dijkstra("habitacion1")
    camino, peso = reconstruir_camino(stack, "habitacion1", "sala_estar")

    print("\nCamino mas corto desde habitacion1 hasta sala_estar:")
    print(" -> ".join(camino))
    print(f"Metros de cable necesarios: {peso}")


# Ejecucion


print("C)")
mst_total()

print("\n D)")
camino_h1_sala()
