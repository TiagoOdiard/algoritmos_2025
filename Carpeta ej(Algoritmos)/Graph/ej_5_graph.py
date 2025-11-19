"""5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
sarios para resolver las tareas, listadas a continuación:

a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
dor, router, switch, impresora;

b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
f. indicar desde que computadora del switch 01 es el camino más corto
al servidor “MongoDB”;
g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
h. debe utilizar un grafo no dirigido."""

from Graph import Graph

g = Graph(is_directed=False)

nodos = {
    # PCs
    'Manjaro': 'pc',
    'Parrot': 'pc',
    'Fedora': 'pc',
    'Mint': 'pc',
    'Ubuntu': 'pc',

    # Notebooks
    'Red Hat': 'notebook',
    'Debian': 'notebook',
    'Arch': 'notebook',

    # Servidores
    'Guaraní': 'servidor',
    'MongoDB': 'servidor',

    # Switches
    'Switch1': 'switch',
    'Switch2': 'switch',

    # Routers
    'Router1': 'router',
    'Router2': 'router',
    'Router3': 'router',

    # Impresora
    'Impresora': 'impresora'
}

# Insertar vertices
for nombre, tipo in nodos.items():
    g.insert_vertex(nombre)
    pos = g.search(nombre, 'value')
    g[pos].other_values = tipo




# Switch1 conexiones
g.insert_edge('Switch1', 'Debian', 17)
g.insert_edge('Switch1', 'Ubuntu', 18)
g.insert_edge('Switch1', 'Mint', 80)
g.insert_edge('Switch1', 'Impresora', 22)

# Router1
g.insert_edge('Router1', 'Switch1', 29)
g.insert_edge('Router1', 'Router2', 37)
g.insert_edge('Router1', 'Router3', 43)

# Router2
g.insert_edge('Router2', 'Red Hat', 25)
g.insert_edge('Router2', 'Guaraní', 9)
g.insert_edge('Router2', 'Router3', 50)

# Router3
g.insert_edge('Router3', 'Switch2', 61)

# Switch2
g.insert_edge('Switch2', 'Manjaro', 40)
g.insert_edge('Switch2', 'Parrot', 12)
g.insert_edge('Switch2', 'MongoDB', 5)
g.insert_edge('Switch2', 'Arch', 56)

# PC Fedora
g.insert_edge('Fedora', 'Switch2', 3)


def reconstruir_camino(stack, origen, destino):
    camino = []
    peso_total = None
    actual = destino
    while stack.size() > 0:
        nodo = stack.pop()   # nombre, costo, predecesor
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



#  B BARRIDOS

def barridos():
    notebooks = ['Red Hat', 'Debian', 'Arch']
    for n in notebooks:
        print("\n DFS DESDE", n, "")
        g.deep_sweep(n)

        print(" BFS DESDE", n, "")
        g.amplitude_sweep(n)



#   C  CAMINO MAS CORTO A IMPRESORA

def camino_impresora():
    pcs = ['Manjaro', 'Red Hat', 'Fedora']
    for pc in pcs:
        stack = g.dijkstra(pc)
        camino, peso = reconstruir_camino(stack, pc, 'Impresora')
        print(f"\nCamino desde {pc} a Impresora: {camino}, peso total = {peso}")



#    D  MST KRUSKAL

def mst():
    print("\nÁRBOL DE EXPANSIÓN MÍNIMA (Kruskal):")
    print(g.kruskal('Manjaro'))



#   E  PC → Servidor Guarani

def pc_mas_cerca_guarani():
    mejores_pc = None
    mejor_peso = None

    for v in g:
        if v.other_values == 'pc':
            stack = g.dijkstra(v.value)
            camino, peso = reconstruir_camino(stack, v.value, 'Guaraní')
            if peso is not None:
                if mejor_peso is None or peso < mejor_peso:
                    mejor_peso = peso
                    mejores_pc = v.value

    print(f"\nLa PC más cercana al servidor Guaraní es: {mejores_pc}, peso = {mejor_peso}")



#F — Desde que PC del Switch1 a MongoDB

def switch1_a_mongodb():
    pos = g.search('Switch1', 'value')
    vecinos = [edge.value for edge in g[pos].edges]

    mejor = None
    mejor_peso = None

    for compu in vecinos:
        stack = g.dijkstra(compu)
        camino, peso = reconstruir_camino(stack, compu, 'MongoDB')
        if peso is not None:
            if mejor_peso is None or peso < mejor_peso:
                mejor_peso = peso
                mejor = compu

    print(f"\nLa computadora del Switch1 con menor camino a MongoDB es: {mejor}, peso = {mejor_peso}")



#   G Cambiar impresora → Router2 y repetir inciso B

def mover_impresora():
    print("\n MOVIENDO IMPRESORA A ROUTER2 ")
    g.delete_edge('Impresora', 'Switch1', 'value')
    g.insert_edge('Impresora', 'Router2', 22)
    print("\n>>> Nuevos barridos desde notebooks:")
    barridos()



#   EJECUCION 
print("\n\n B) ")
barridos()

print("\n\n  C) ")
camino_impresora()

print("\n\n D) ")
mst()

print("\n\n E) ")
pc_mas_cerca_guarani()

print("\n\n  F) ")
switch1_a_mongodb()

print("\n\n G) ")
mover_impresora()


