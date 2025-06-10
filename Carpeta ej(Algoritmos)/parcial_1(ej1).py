#Ejercicio numero 1 

superheroes = [
    "iron man", "hulk", "thor", "spider Man", "black widow",
    "hawkeye", "pantera negra", "super man", "hombre hormiga",
    "Linterna verde", "mujer maravilla", "vision", "el alcon", "wolverine",
    "Capitan America"
]


def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_capitan(lista, indice + 1)


def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)


print("¿Está Capitan America en la lista?")
if buscar_capitan(superheroes):
    print("Sí, está en la lista.")
else:
    print("No, no está en la lista.")

print("Listado de superhéroes:")
listar_superheroes(superheroes)

