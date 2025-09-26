#Ejercicio 10
from queue_ import Queue
from stack import Stack

#Cada notificación es un diccionario con: hora, app y mensaje


# a) eliminar todas las notificaciones de Facebook
def eliminar_facebook(c: Queue) -> None:
    aux = Queue()
    while c.size() > 0:
        notif = c.attention()
        if notif["app"] != "Facebook":
            aux.arrive(notif)
    # restauracion en la cola original
    while aux.size() > 0:
        c.arrive(aux.attention())

# b) mostrar notificaciones de Twitter con "Python" sin perder datos
def mostrar_twitter_python(c: Queue) -> None:
    for _ in range(c.size()):
        notif = c.move_to_end()
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(notif)

# c) usar pila para contar notificaciones entre 11:43 y 15:57
def contar_intervalo(c: Queue, inicio="11:43", fin="15:57") -> int:
    pila = Stack()
    contador = 0
    for _ in range(c.size()):
        notif = c.move_to_end()
        if inicio <= notif["hora"] <= fin:
            pila.push(notif)
            contador += 1
    return contador

#Ejecucion
if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"hora": "10:15", "app": "Facebook", "mensaje": "Hola"})
    cola.arrive({"hora": "12:00", "app": "Twitter", "mensaje": "Aprendiendo Python"})
    cola.arrive({"hora": "14:30", "app": "Instagram", "mensaje": "Nueva foto"})
    cola.arrive({"hora": "16:00", "app": "Twitter", "mensaje": "Otro tweet"})
    cola.arrive({"hora": "13:20", "app": "Twitter", "mensaje": "Python es genial!"})

    print("Cola inicial:")
    cola.show()

    print("Eliminar Facebook:")
    eliminar_facebook(cola)
    cola.show()

    print("Notificaciones de Twitter con 'Python':")
    mostrar_twitter_python(cola)

    print("Cantidad de notificaciones entre 11:43 y 15:57:")
    print(contar_intervalo(cola))



#Ejercicio 22

# a) determinar el nombre del personaje de la superhéroe Capitana Marvel
def personaje_capitana_marvel(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["superheroe"] == "Capitana Marvel":
            return dato["personaje"]
    return "No encontrado"

# b) mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["genero"] == "F":
            print(dato["superheroe"])

# c) mostrar los nombres de los personajes masculinos
def personajes_masculinos(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["genero"] == "M":
            print(dato["personaje"])

# d) determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_scott_lang(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"] == "Scott Lang":
            return dato["superheroe"]
    return "No encontrado"

# e) mostrar todos los datos de los que comienzan con S (personaje o superhéroe)
def comienzan_con_s(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print(dato)

# f) determinar si Carol Danvers está y mostrar su superhéroe
def carol_danvers(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"] == "Carol Danvers":
            return f"Está en la cola, su superhéroe es {dato['superheroe']}"
    return "Carol Danvers no se encuentra en la cola"


#Ejecucion
if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
    cola.arrive({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
    cola.arrive({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
    cola.arrive({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
    cola.arrive({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
    cola.arrive({"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"})

    print("a)", personaje_capitana_marvel(cola))
    print("b) Superhéroes femeninos:")
    superheroes_femeninos(cola)

    print("c) Personajes masculinos:")
    personajes_masculinos(cola)

    print("d)", superheroe_scott_lang(cola))

    print("e) Comienzan con S:")
    comienzan_con_s(cola)

    print("f)", carol_danvers(cola))
