from tree import BinaryTree


#Lista de pokemones:


pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["planta", "veneno"],
     "debilidades": ["fuego", "hielo", "psiquico", "volador"],
     "mega": False, "gigamax": False},

    {"nombre": "Charmander", "numero": 4, "tipos": ["fuego"],
     "debilidades": ["agua", "tierra", "roca"],
     "mega": False, "gigamax": False},

    {"nombre": "Charizard", "numero": 6, "tipos": ["fuego", "volador"],
     "debilidades": ["agua", "electrico", "roca"],
     "mega": True, "gigamax": True},

    {"nombre": "Squirtle", "numero": 7, "tipos": ["agua"],
     "debilidades": ["electrico", "planta"],
     "mega": False, "gigamax": False},

    {"nombre": "Pikachu", "numero": 25, "tipos": ["electrico"],
     "debilidades": ["tierra"],
     "mega": False, "gigamax": True},

    {"nombre": "Raichu", "numero": 26, "tipos": ["electrico"],
     "debilidades": ["tierra"],
     "mega": False, "gigamax": False},

    {"nombre": "Gengar", "numero": 94, "tipos": ["fantasma", "veneno"],
     "debilidades": ["psiquico", "fantasma", "siniestro"],
     "mega": True, "gigamax": True},

    {"nombre": "Steelix", "numero": 208, "tipos": ["acero", "tierra"],
     "debilidades": ["agua", "fuego", "lucha", "tierra"],
     "mega": True, "gigamax": False},

    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["roca", "dragon"],
     "debilidades": ["hielo", "lucha", "dragon", "hada"],
     "mega": False, "gigamax": False},

    {"nombre": "Lycanroc", "numero": 745, "tipos": ["roca"],
     "debilidades": ["agua", "planta", "acero", "lucha", "tierra"],
     "mega": False, "gigamax": False},

    {"nombre": "Jolteon", "numero": 135, "tipos": ["electrico"],
     "debilidades": ["tierra"],
     "mega": False, "gigamax": False},
]


#Arboles:

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for p in pokemons:
    arbol_nombre.insert(p["nombre"], p)
    arbol_numero.insert(p["numero"], p)

   
    for t in p["tipos"]:
        nodo_tipo = arbol_tipo.search(t)
        if nodo_tipo is None:
            
            arbol_tipo.insert(t, [p])
        else:
            if isinstance(nodo_tipo.other_values, list):
                if not any(existing["nombre"] == p["nombre"] for existing in nodo_tipo.other_values):
                    nodo_tipo.other_values.append(p)
            else:
                nodo_tipo.other_values = [nodo_tipo.other_values, p]


# A) Bucar por numeros y mostrar sus datos


def buscar_por_numero(num):
    nodo = arbol_numero.search(num)
    if nodo:
        print(f"\nDatos del Pokemon #{num}:")
        print(nodo.other_values)
    else:
        print(f"\nNo se encontro Pokemon con numero {num}")


# B) Bucar por proximidad “bul”


def buscar_por_nombre_proximidad(subcadena):
    sub = subcadena.lower()
    resultados = []

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            if sub in str(root.value).lower():
                resultados.append(root.other_values)
            recorrer(root.right)

    if arbol_nombre.root is not None:
        recorrer(arbol_nombre.root)

    print(f"\nPokemon cuyos nombres contienen '{subcadena}':")
    if resultados:
        for r in resultados:
            print(f"- {r['nombre']} (#{r['numero']})")
    else:
        print("Ninguno")


# C) Mostrar pokemones de tipos especificos


def pokemons_por_tipo(tipo):
    nodo = arbol_tipo.search(tipo)
    print(f"\n Pokemon del tipo '{tipo}':")
    if nodo and isinstance(nodo.other_values, list) and nodo.other_values:
        vistos = set()
        for p in nodo.other_values:
            if p["nombre"] not in vistos:
                vistos.add(p["nombre"])
                print(f"- {p['nombre']} (#{p['numero']}) - tipos: {p['tipos']}")
    else:
        print("Ninguno")


# D) Listado ascendente ordenado por numero y nombre


def listado_ordenado():
    print("\nPokemon ordenados por numero (in-order en arbol de numeros):")
    arbol_numero.in_order()

    print("\nPokemon ordenados por nombre (in-order en arbol de nombres):")
    arbol_nombre.in_order()

    print("\nListado por niveles (arbol de nombres):")
    arbol_nombre.by_level()


# E) Pokemones debiles a Jolteon, Lycanroc Y Tyrantrum
# (Se considera debil si en sus 'debilidades' aparece algun tipo del objetivo)


def debiles_a(lista_objetivo):
    for nombre in lista_objetivo:
        nodo_obj = arbol_nombre.search(nombre)
        if nodo_obj:
            tipos_obj = nodo_obj.other_values["tipos"]
            print(f"\nPokemon debiles frente a {nombre} (tipos del objetivo: {tipos_obj}):")
            encontrados = False
            for p in pokemons:
                if any(t in p["debilidades"] for t in tipos_obj):
                    print(f"- {p['nombre']} (#{p['numero']}) debilidades: {p['debilidades']}")
                    encontrados = True
            if not encontrados:
                print("Ninguno")
        else:
            print(f"\nObjetivo '{nombre}' no encontrado en el arbol de nombres")


# F)Cuantos hay de cada tipo:

def contar_tipos():
    contador = {}
    for p in pokemons:
        for t in p["tipos"]:
            contador[t] = contador.get(t, 0) + 1
    print("Cantidad de pokemon por tipo:")
    for t, c in contador.items():
        print(f"- {t}: {c}")


# G) Cuantos tienen Megaevolucion


def contar_mega():
    total = sum(1 for p in pokemons if p["mega"])
    print(f"\nPokemon con megaevolución: {total}")


# H) Cuantos tienen Gigamax


def contar_gigamax():
    total = sum(1 for p in pokemons if p["gigamax"])
    print(f"\nPokemon con Gigamax: {total}")


# Ejecucion


buscar_por_numero(6)
buscar_por_nombre_proximidad("bul")  

for t in ["fantasma", "fuego", "acero", "electrico"]:
    pokemons_por_tipo(t)

listado_ordenado()

debiles_a(["Jolteon", "Lycanroc", "Tyrantrum"])

contar_tipos()
contar_mega()
contar_gigamax()
