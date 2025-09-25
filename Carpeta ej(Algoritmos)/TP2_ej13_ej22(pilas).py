from stack import Stack

#Ejercicio 13(pila)
# Definimos un traje 
def crear_traje(modelo, pelicula, estado):
    return {
        "modelo": modelo,
        "pelicula": pelicula,
        "estado": estado
    }

# Cargamos la pila 
pila_trajes = Stack()
pila_trajes.push(crear_traje("Mark III", "Iron Man", "Dañado"))
pila_trajes.push(crear_traje("Mark XLIV", "Avengers: Age of Ultron", "Impecable"))  # Hulkbuster
pila_trajes.push(crear_traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"))
pila_trajes.push(crear_traje("Mark XLVI", "Capitan America: Civil War", "Destruido"))
pila_trajes.push(crear_traje("Mark L", "Avengers: Infinity War", "Impecable"))

# a) Verificar si el modelo Hulkbuster aparece y mostrar sus películas
def buscar_hulkbuster(pila):
    aux = Stack()
    encontrado = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            print(f"El modelo Hulkbuster fue usado en: {traje['pelicula']}")
            encontrado = True
        aux.push(traje)
    
    # Aca se restaura la pila
    while aux.size() > 0:
        pila.push(aux.pop())
    if not encontrado:
        print("El modelo Hulkbuster no fue encontrado.")

# b) Mostrar los modelos dañados
def mostrar_dañados(pila):
    aux = Stack()
    print("Modelos dañados:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            print(traje["modelo"], "-", traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# c) Eliminar los destruidos
def eliminar_destruidos(pila):
    aux = Stack()
    print("Eliminando modelos destruidos:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            print("Eliminado:", traje["modelo"], "-", traje["pelicula"])
        else:
            aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# e) Agregar Mark LXXXV si no está en la misma película
def agregar_mark_lxxxv(pila, pelicula):
    aux = Stack()
    repetido = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == pelicula:
            repetido = True
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if not repetido:
        pila.push(crear_traje("Mark LXXXV", pelicula, "Impecable"))
        print("Mark LXXXV agregado en", pelicula)
    else:
        print("Mark LXXXV ya estaba en esa película.")

# f) Mostrar trajes de dos películas específicas
def mostrar_trajes_peliculas(pila, peliculas):
    aux = Stack()
    print(f"Trajes usados en {peliculas}:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in peliculas:
            print(traje["modelo"], "-", traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())



# Ejecución
buscar_hulkbuster(pila_trajes)
print()
mostrar_dañados(pila_trajes)
print()
eliminar_destruidos(pila_trajes)
print()
agregar_mark_lxxxv(pila_trajes, "Avengers: Endgame")
print()
mostrar_trajes_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Capitan America: Civil War"])

        
#Ejercicio 24(Pila)

# Definicion de un personaje 
def crear_personaje(nombre, cant_peliculas):
    return {
        "nombre": nombre,
        "peliculas": cant_peliculas
    }

# Creacion de la pila 
pila_personajes = Stack()
pila_personajes.push(crear_personaje("Iron Man", 10))
pila_personajes.push(crear_personaje("Captain America", 9))
pila_personajes.push(crear_personaje("Thor", 9))
pila_personajes.push(crear_personaje("Black Widow", 8))
pila_personajes.push(crear_personaje("Hawkeye", 5))
pila_personajes.push(crear_personaje("Rocket Raccoon", 4))
pila_personajes.push(crear_personaje("Groot", 4))
pila_personajes.push(crear_personaje("Doctor Strange", 5))
pila_personajes.push(crear_personaje("Captain Marvel", 2))
pila_personajes.push(crear_personaje("Gamora", 4))

# a) Determinar posición de Rocket Raccoon y Groot
def buscar_posiciones(pila, nombres):
    aux = Stack()
    posiciones = {}
    pos = 1
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] in nombres:
            posiciones[personaje["nombre"]] = pos
        aux.push(personaje)
        pos += 1
    # Restauracion de pila
    while aux.size() > 0:
        pila.push(aux.pop())
    return posiciones

# b) Personajes con más de 5 películas
def mas_de_cinco(pila):
    aux = Stack()
    print("Personajes con más de 5 películas:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            print(f"{personaje['nombre']} - {personaje['peliculas']} películas")
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())

# c) Cuántas películas hizo Black Widow
def peliculas_black_widow(pila):
    aux = Stack()
    cantidad = None
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if cantidad is not None:
        print("Black Widow participó en", cantidad, "películas")
    else:
        print("Black Widow no está en la pila.")

# d) Mostrar personajes cuyos nombres empiezan con C, D o G
def personajes_iniciales(pila, letras):
    aux = Stack()
    print(f"Personajes cuyos nombres empiezan con {', '.join(letras)}:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"][0] in letras:
            print(personaje["nombre"])
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())


# Ejecución
posiciones = buscar_posiciones(pila_personajes, ["Rocket Raccoon", "Groot"])
print("Posiciones de Rocket y Groot:", posiciones)
print()

mas_de_cinco(pila_personajes)
print()

peliculas_black_widow(pila_personajes)
print()

personajes_iniciales(pila_personajes, ["C", "D", "G"])
