"""6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

from list_ import List

class SuperHero:
    def __init__(self,name,year,house,biography):
        self.name = name
        self.year = year
        self.house = house
        self.biography = biography
        
    def __str__(self):
        return f'Nombre: {self.name}, Año: {self.year}, Casa: {self.house}, Biografia: {self.biography}'

superheros = List()
superheros.add_criterion('name', lambda n: n.name)
superheros.add_criterion('year', lambda n: n.year)
superheros.add_criterion('house', lambda n: n.house)
superheros.add_criterion('biography', lambda n: n.biography)

superheros.extend(
    [
        SuperHero(
            "Linterna Verde",
            1940,
            "DC",
            "Posee un anillo de poder y viste un traje especial.",
        ),
        SuperHero(
            "Wolverine",
            1974,
            "Marvel",
            "Tiene garras retráctiles y factor de curación.",
        ),
        SuperHero("Dr. Strange", 1963, "DC", "Usa magia y viste una túnica."),
        SuperHero(
            "Iron Man",
            1963,
            "Marvel",
            "Tony Stark usa una armadura de alta tecnología.",
        ),
        SuperHero("Capitana Marvel", 1968, "Marvel", "Tiene poderes cósmicos."),
        SuperHero(
            "Mujer Maravilla", 1941, "DC", "Princesa amazona con traje de batalla."
        ),
        SuperHero("Flash", 1940, "DC", "Corre a velocidades increíbles."),
        SuperHero("Star-Lord", 1976, "Marvel", "Usa una máscara y armadura espacial."),
        SuperHero(
            "Batman", 1939, "DC", "Lucha contra el crimen con traje de murciélago."
        ),
        SuperHero("Spider-Man", 1962, "Marvel", "Lleva un traje rojo y azul."),
        SuperHero(
            "Magneto", 1963, "Marvel", "Controla el magnetismo y usa casco y armadura."
        ),
        SuperHero("Superman", 1938, "DC", "Traje azul con capa roja."),
    ]
)

#A Eliminar la informacion de linterna verde
def delete_char(superhero: List):
    superhero.delete_value("Linterna Verde", "name")
         
print('A)')
delete_char(superheros)
superheros.show()

#B Mostrar el año de aparición de Wolverine
def serch_wolverine(superhero: List):
    index = superhero.search("Wolverine","name")
    if index is not None:
        return print(f'El año de aparicion de wolverine : {superhero[index].year}')
    else:
        return print('Wolverine no esta en la lista')

print()
print('B)')
serch_wolverine(superheros)

#C Cambiar la casa de Dr. Strange a Marvel;
def change_dr_strange(superhero: List):
    index = superhero.search("Dr. Strange","name")
    if index is not None:
       superhero[index].house = 'Marvel'
       print('Se modifico la casa del Dr. Strange')
       print(superhero[index]) 
    else:
        print('No se encontro al Dr. Strange en la lista') 
        
print()
print('C)')
change_dr_strange(superheros)

#D Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
def print_names(superhero: List):
    for hero in superhero:
        bio = hero.biography.lower()
        if 'traje' in bio or 'armadura' in bio:
            print(hero.name)
        
print()
print('D)')
print('Personajes que usan traje o armadura: ')
print_names(superheros)        

#E Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
def year_1963(superheros):
    for hero in superheros:
        if hero.year < 1963:
            print(f'{hero.name}-{hero.house}')
            
print()
print('E)')
print('Personajes que aparecieron antes de 1963')
year_1963(superheros)

#F Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
def serch_house(superheros: List, hero):
    index = superheros.search(hero,"name")
    return  superheros[index].house
    
print()
print('F)')
print(f'La casa de Capitana Marvel es: {serch_house(superheros,"Capitana Marvel")}')
print(f'La casa de la Mujer Maravilla es: {serch_house(superheros,"Mujer Maravilla")}')
        
#G Mostrar toda la información de Flash y Star-Lord        
def show_information(superheros: List,name):
    index = superheros.search(name,"name")
    
    return superheros[index]
print()
print('G)')
print(f'La informacion de Flash es: {show_information(superheros,'Flash')}')
print(f'La informacion de Flash es: {show_information(superheros,'Star-Lord')}')

#H Listar los superhéroes que comienzan con la letra B, M y S
def show_heros_BMS(superheros:List):
    
    for hero in superheros:
        name = hero.name
        if name.startswith(('B','M','S')):
            print(hero.name)
        
print()
print('H)')
show_heros_BMS(superheros)       
        
#I Determinar cuántos superhéroes hay de cada casa de comic.
def cont_comicts(superheros: List):
    contMar = 0
    contDC = 0
    for hero in superheros:
        if hero.house == 'DC':
            contDC += 1
        
        if hero.house == 'Marvel':
            contMar += 1
            
    return contMar,contDC

contMar,contDC = cont_comicts(superheros)
print()
print('I)')
print(f'La cantidad de superheroes en DC son {contDC}')
print(f'La cantidad de superheroes en Marvel son {contMar}'
