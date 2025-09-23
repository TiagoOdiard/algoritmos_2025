from list_ import List

jedi = List([
    {"nombre": "Yoda", "maestros": [], "sables": ["verde"], "especie": "desconocida"},
    {"nombre": "Luke Skywalker", "maestros": ["Obi-Wan Kenobi", "Yoda"], "sables": ["azul", "verde"], "especie": "humano"},
    {"nombre": "Anakin Skywalker", "maestros": ["Obi-Wan Kenobi"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Obi-Wan Kenobi", "maestros": ["Qui-Gon Jinn"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Conde Dooku"], "sables": ["verde"], "especie": "humano"},
    {"nombre": "Mace Windu", "maestros": ["Cyslin Myr"], "sables": ["violeta"], "especie": "humano"},
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], "sables": ["verde", "azul", "blanco"], "especie": "togruta"},
    {"nombre": "Kit Fisto", "maestros": [], "sables": ["verde"], "especie": "nautolano"},
    {"nombre": "Plo Koon", "maestros": [], "sables": ["naranja"], "especie": "kel dor"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], "sables": ["azul"], "especie": "twi'lek"},
])


jedi.add_criterion("nombre", lambda j: j["nombre"])
jedi.add_criterion("especie", lambda j: j["especie"])


# a) Listado por nombre y especie
print("a) Jedi ordenados por nombre:")
jedi.sort_by_criterion("nombre")
for j in jedi:
    print(j["nombre"])

print("Jedi ordenados por especie:")
jedi.sort_by_criterion("especie")
for j in jedi:
    print("-" ,j["nombre"], "(", j["especie"], ")")


# b) Info de Ahsoka Tano y Kit Fisto
print("b) Info de Ahsoka Tano y Kit Fisto:")
for name in ["Ahsoka Tano", "Kit Fisto"]:
    idx = jedi.search(name, "nombre")
    if idx is not None:
        print("-", jedi[idx])


# c) Padawan de Yoda y Luke Skywalker
print("c) Padawans de Yoda y Luke Skywalker:")
for maestro in ["Yoda", "Luke Skywalker"]:
    print(f"{maestro}:")
    for j in jedi:
        if maestro in j["maestros"]:
            print("  -", j["nombre"])


# d) Jedi humanos y twi'lek
print("d) Jedi humanos y twi'lek:")
for j in jedi:
    if j["especie"].lower() in ["humano", "twi'lek"]:
        print("-", j["nombre"], "(", j["especie"], ")")


# e) Jedi que comienzan con A
print("e) Jedi que comienzan con A:")
for j in jedi:
    if j["nombre"].startswith("A"):
        print("-", j["nombre"])


# f) Jedi con más de un color de sable
print("f) Jedi con más de un color de sable:")
for j in jedi:
    if len(j["sables"]) > 1:
        print("-", j["nombre"], "->", j["sables"])


# g) Jedi que usaron sable amarillo o violeta
print("g) Jedi con sable amarillo o violeta:")
for j in jedi:
    if "amarillo" in j["sables"] or "violeta" in j["sables"]:
        print("-", j["nombre"], "->", j["sables"])
        

# h) Padawans de Qui-Gon Jinn y Mace Windu
print("h) Padawans de Qui-Gon Jinn y Mace Windu:")
for maestro in ["Qui-Gon Jinn", "Mace Windu"]:
    print(f"{maestro}:")
    encontrados = False
    for j in jedi:
        if maestro in j["maestros"]:
            print("  -", j["nombre"])
            encontrados = True
    if not encontrados:
        print("  (sin padawans)")
