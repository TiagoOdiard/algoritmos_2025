"""22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:

a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron."""

from list_ import List

class jedi:
    
    def __init__(self,name,master,sable_color,especie):
        self.name = name
        self.master = master
        self.sable_color = sable_color
        self.especie = especie
        
    def __str__(self):
        return f"Nombre: {self.name}, Especie: {self.especie}, Sable: {self.sable_color}, Maestro: {self.master}"
    
jedi_list = [
    jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "Humano"),
    jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul"], "Humano"),
    jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn", "Yoda"], ["azul"], "Humano"),
    jedi("Yoda", [], ["verde"], "Desconocida"),
    jedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul", "blanco"], "Togruta"),
    jedi("Kit Fisto", ["Yoda"], ["verde"], "Nautolano"),
    jedi("Qui-Gon Jinn", ["Dooku"], ["verde"], "Humano"),
    jedi("Mace Windu", ["Cyslin Myr"], ["violeta"], "Humano"),
    jedi("Plo Koon", ["Tyvokka"], ["naranja"], "Kel Dor"),
    jedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "Twi'lek"),
    jedi("Luminara Unduli", ["Yoda"], ["verde"], "Mirialana"),
    jedi("Barriss Offee", ["Luminara Unduli"], ["azul"], "Mirialana"),
    jedi("Adi Gallia", ["Phanius"], ["rojo", "azul"], "Tholothiana"),
    jedi("Shaak Ti", ["Yoda"], ["azul"], "Togruta"),
    jedi("Rey", ["Leia Organa", "Luke Skywalker"], ["azul", "amarillo"], "Humana")
]

jedis = List()

jedis.add_criterion('name', lambda jedi:jedi.name)
jedis.add_criterion('especie', lambda jedi:jedi.especie)
    
for jed in jedi_list:
    jedis.append(jed)

#A Listado ordenado por nombre y por especie
print('A)Listado por nombre:')
jedis.sort_by_criterion('name')
jedis.show()    
print()
print('Listado por especie:')
jedis.sort_by_criterion('especie')
jedis.show()
print() 

#B Mostrar toda la información de Ahsoka Tano y Kit Fisto.
def search_char(char):
    for i in jedis:
        if i.name == char:
            print(i)
print()            
print('B)')
print('Informacion de Ahsoka Tano')
search_char('Ahsoka Tano')        
print('Informacion de Kit Fisto')
search_char('Kit Fisto')

#C Mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices.
def search_aprendiz(master):
    for jedi in jedis:
        if master in jedi.master:
            print(jedi.name)
print()            
print('C)')
print('Aprendices de Yoda:')
search_aprendiz('Yoda')
print()
print('Aprendizes de Luke Skywalker:')
search_aprendiz('Luke Skywalker')

#D Mostrar los Jedi de especie humana y twi'lek
def specie(especie):
    for jedi in jedis:
        if especie == jedi.especie:
            print(jedi.name)
            
print()
print('D)')
print('Jedi de especie humana: ')
specie('Humano')
print()
print('Jedi especie twi lek: ')
specie("Twi'lek")

#E Listar todos los Jedi que comienzan con 'A'
def jedi_a(letra):
    for jedi in jedis:
        if jedi.name.startswith(letra):
            print(jedi.name)
print()
print('E)')
print(f"Jedis cuyo nombre comienza con la letra 'A': ")
jedi_a('A')

#F Mostrar los Jedi que usaron sable de luz de más de un color
def cont_sables(jedis):
    for jedi in jedis:
        if len(jedi.sable_color) > 1:
            print(jedi.name, jedi.sable_color)
            
print()
print('F)')
print('Jedis que usaron mas de un color de luz: ')
cont_sables(jedis)

#G Indicar los Jedi que utilizaron sable de luz amarillo o violeta
def search_color(color):
    for jedi in jedis:
        if color in jedi.sable_color:
            print(jedi.name, jedi.sable_color)
            
print()
print('G)')
print('Jedis que usaron sable de luz amarillo: ')
search_color("amarillo")
print('Jedis que usaron sable de color violeta: ')
search_color("violeta")

#H Indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron 
def padawans(master):
    padawans = []
    for jedi in jedis:
        if master in jedi.master:
            padawans.append(jedi.name)
    return padawans


padawans_qui = padawans("Qui-Gon Jinn")
padawans_mace = padawans("Mace Windu")

print()
print('H)')
if padawans_qui:
    print("Padawans de Qui-Gon Jin:")
    if padawans_qui:
        for padawan in padawans_qui:
            print(padawan)
else:
    print("Qui-Gon Jin no tuvo padawans.")

if padawans_mace:
    print("Padawans de Mace Windu:")
    if padawans_mace:
        for padawan in padawans_mace:
            print(padawan)
else:
    print("Mace Windu no tuvo padawans.")
