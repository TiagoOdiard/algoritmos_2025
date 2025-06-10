#Ejercicio 2

from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue


lista_personajes = List(superheroes)


lista_personajes.add_criterion("name", lambda p: p["name"])
lista_personajes.add_criterion("real_name", lambda p: p["real_name"] or "")
lista_personajes.add_criterion("first_appearance", lambda p: p["first_appearance"])

# A. 
lista_personajes.sort_by_criterion("name")
print("A. Personajes ordenados por nombre:")
for p in lista_personajes:
    print(p["name"])

print("-----------------------------------------------")

# B. 
pos_thing = lista_personajes.search("The Thing", "name")
pos_rocket = lista_personajes.search("Rocket Raccoon", "name")
print(f"B. The Thing está en la posición: {pos_thing}")
print(f"   Rocket Raccoon está en la posición: {pos_rocket}")

print("-----------------------------------------------")

# C. 
villanos = List([p for p in lista_personajes if p["is_villain"]])
print("C. Villanos:")
for v in villanos:
    print(v["name"])

print("-----------------------------------------------")

# D. 
cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

print("D. Villanos que aparecieron antes de 1980:")
for i in range(cola_villanos.size()):
    villano = cola_villanos.move_to_end()
    if villano["first_appearance"] < 1980:
        print(villano["name"])

print("-----------------------------------------------")

# E. 
print("E. Superhéroes que comienzan con Bl, G, My o W:")
for p in lista_personajes:
    if p["name"].startswith(("Bl", "G", "My", "W")):
        print(p["name"])

print("-----------------------------------------------")

# F. 
lista_personajes.sort_by_criterion("real_name")
print("F. Personajes ordenados por nombre real (ascendente):")
for p in lista_personajes:
    print(f"{p['real_name']} → {p['name']}")

print("-----------------------------------------------")

# G. 
lista_personajes.sort_by_criterion("first_appearance")
print("G. Personajes ordenados por aparición:")
for p in lista_personajes:
    print(f"{p['name']} ({p['first_appearance']})")

print("-----------------------------------------------")

# H. 
for p in lista_personajes:
    if p["name"] == "Ant Man":
        p["real_name"] = "Scott Lang"
        print(f"H. Nuevo nombre real de Ant Man: {p['real_name']}")
        break

print("-----------------------------------------------")

# I. 
print("I. Personajes con 'time-traveling' o 'suit' en la biografía:")
for p in lista_personajes:
    bio = p["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(p["name"])

print("-----------------------------------------------")

# J. 
print("J. Información de personajes eliminados:")

for nombre in ["Electro", "Baron Zemo"]:
    eliminado = lista_personajes.delete_value(nombre, "name")
    if eliminado:
        print(f"{eliminado['name']}:")
        for clave, valor in eliminado.items():
            print(f"  {clave}: {valor}")
    else:
        print(f"{nombre} no se encontraba en la lista.")
