from Graph import Graph


# 1) Creacion del grafo y lista de personajes

g = Graph(is_directed=False)

personajes = {
    "Luke Skywalker": [1,2,3,4,5,6,7],
    "Darth Vader":    [1,2,3,4,5,6],
    "Yoda":           [2,3,4,5,6,8],
    "Boba Fett":      [5,6],
    "C-3PO":          list(range(1,10)),   # aparece en los 9
    "Leia":           [1,2,3,4,5,6,7,8],
    "Rey":            [7,8,9],
    "Kylo Ren":       [7,8,9],
    "Chewbacca":      list(range(1,10)),   # aparece en los 9
    "Han Solo":       [1,2,3,4,5,6,7],
    "R2-D2":          list(range(1,10)),   # aparece en los 9
    "BB-8":           [7,8,9],
}

# Insercion de vertices
for p in personajes:
    g.insert_vertex(p)
    pos = g.search(p, 'value')
    g[pos].other_values = {"episodios": personajes[p]}

# Insercion de aristas peso = episodios compartidos
nombres = list(personajes.keys())

for i in range(len(nombres)):
    for j in range(i+1, len(nombres)):
        p1 = nombres[i]
        p2 = nombres[j]
        compartidos = len(set(personajes[p1]).intersection(personajes[p2]))
        if compartidos > 0:
            g.insert_edge(p1, p2, compartidos)


# 2) Arbol de expansion minimo (Kruskal) desde 3 personajes


print("\n- Arbol de expansion minimo desde C-3PO -")
print(g.kruskal("C-3PO"))

print("\n- Arbol de expansión minimo desde Yoda -")
print(g.kruskal("Yoda"))

print("\n- Arbol de expansión minimo desde Leia -")
print(g.kruskal("Leia"))


# 3) Maximo numero de episodios compartidos entre 2 personajes

print("\n- Maximo numero de episodios compartidos -")

maximo = 0
pares = []

for v in g:
    for e in v.edges:
        w = e.weight
        if w > maximo:
            maximo = w
            pares = [(v.value, e.value)]
        elif w == maximo:
            pares.append((v.value, e.value))

print("Maximo:", maximo)
print("Pares:")
for a, b in pares:
    print("-", a, "<->", b)


# 4) Camino mas corto usando DIJKSTRA

def camino_mas_corto(grafo, origen, destino):
    print(f"\n- Camino mas corto de {origen} a {destino} -")

    pila = grafo.dijkstra(origen)
    actual = destino
    camino = []
    costo = None

    while pila.size() > 0:
        nodo = pila.pop()
        nombre = nodo[0]
        distancia = nodo[1]
        anterior = nodo[2]

        if nombre == actual:
            if costo is None:
                costo = distancia
            camino.append(nombre)
            actual = anterior

    camino.reverse()
    print("Camino:", " -> ".join(camino))
    print("Costo:", costo)


camino_mas_corto(g, "C-3PO", "R2-D2")
camino_mas_corto(g, "Yoda", "Darth Vader")

# 5) Personajes que aparecieron en los 9 episodios

print("\n- Personajes que aparecieron en los 9 episodios -")
for v in g:
    if len(v.other_values["episodios"]) == 9:
        print("-", v.value)
