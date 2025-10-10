"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra "Python", si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from queue_ import Queue
from stack import Stack

queue = Queue()

queue.arrive({"hour": "10:30", "app": "Facebook", "message": "Nuevo comentario"})
queue.arrive({"hour": "11:00", "app": "Twitter", "message": "Aprendiendo Java!"})
queue.arrive({"hour": "12:00", "app": "Facebook", "message": "Nuevo like"})
queue.arrive({"hour": "13:00", "app": "Twitter", "message": "Python es increíble"})
queue.arrive({"hour": "14:00", "app": "Instagram", "message": "Nueva foto publicada"})
queue.arrive({"hour": "15:00", "app": "Facebook", "message": "Nuevo mensaje privado"})

#A)
def del_facebook(queue: Queue):
    
    for i in range(queue.size()):
        
        noti = queue.attention()
        if noti["app"] != "Facebook":
           queue.arrive(noti)
           
    return queue

#B)
def twitter(queue):
    aux_queue = Queue()
    word = 'Python'
    
    while queue.size() > 0:
        noti = queue.attention()
        
        if noti["app"] == 'Twitter' and word in noti["message"]:
           print(noti)
        
        aux_queue.arrive(noti)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())

#C)
def hour_messages(queue: Queue):
    stack = Stack()
    cont = 0
    
    while queue.size() > 0:
        noti = queue.attention()
        
        if noti["hour"] >= "11:43" and noti["hour"] <= "15:57":
            stack.push(noti)
            cont += 1
    
    while stack.size() > 0:
        queue.arrive(stack.pop())
    
    return cont

print("a) ")
del_facebook(queue).show()

print("b) ")
twitter(queue)

print(f"c) Notificaciones producidas entre las 11:43 y las 15:57: {hour_messages(queue)}")


""" 22.
    Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género 
    (Masculino M y FemeninoF), por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
    desarrollar un algoritmo que resuelva las siguientes actividades:
    a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    b. mostrar los nombre de los superhéroes femeninos;
    c. mostrar los nombres de los personajes masculinos;
    d. determinar el nombre del superhéroe del personaje Scott Lang;
    e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
    f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""
queue = Queue()

queue.arrive({"name": "Tony Stark", "superhero": "Iron Man", "gender": "M"})
queue.arrive({"name": "Steve Rogers", "superhero": "Capitán América", "gender": "M"})
queue.arrive({"name": "Natasha Romanoff", "superhero": "Black Widow", "gender": "F"})
queue.arrive({"name": "Carol Danvers", "superhero": "Capitana Marvel", "gender": "F"})
queue.arrive({"name": "Scott Lang", "superhero": "Ant-Man", "gender": "M"})
queue.arrive({"name": "Bruce Banner", "superhero": "Hulk", "gender": "M"})
queue.arrive({"name": "Clint Barton", "superhero": "Hawkeye", "gender": "M"})
queue.arrive({"name": "Wanda Maximoff", "superhero": "Scarlet Witch", "gender": "F"})

#A
def identify_caharacter(queue: Queue, name):
    
    for i in range(queue.size()):
        charater = queue.attention()
        
        if charater["superhero"] == name:
            char = charater["name"]
    
        queue.arrive(charater)
    return char

print('A)Nombre de capitana Marvel:')
print(identify_caharacter(queue, "Capitana Marvel"))

#B
def identify_names_F(queue: Queue):
    for i in range(queue.size()):
        char = queue.attention()
        if char["gender"] == "F":
            print(f'{char["name"]} - {char["superhero"]} ')
               
        queue.arrive(char)
        
print("B)Nombres femeninos: ")
identify_names_F(queue)
            
#C
def identify_names_M(queue: Queue):
    
    for i in range(queue.size()):
        char = queue.attention()
        if char["gender"] == "M":
            print(f'{char["name"]} - {char["superhero"]} ')
               
        queue.arrive(char)

print("C) Nombres Masculinos: ")
identify_names_M(queue)

#D
def serch_scott_lang(queue: Queue):
    for i in range(queue.size()):
        char = queue.attention()
        if char["name"] == "Scott Lang":
            print(f'{char["name"]} es: {char["superhero"]}')
            
        queue.arrive(char)
        
print('D) Buscar a Scott Lang en la cola')
serch_scott_lang(queue)

#E
def superhero_with_s(queue: Queue):
    new_queue = Queue()
    
    for i in range(queue.size()):
        char = queue.attention()
        
        if char["name"][0] == 'S' or char["superhero"][0] == "S":
            new_queue.arrive(char)
            
        queue.arrive(char)
        
    return new_queue

print('E) Nombre o superheroes que comienzan con "S" ')
superhero_with_s(queue).show()

#F
def serch_character(queue: Queue,name):
    for i in range (queue.size()):
        char = queue.attention()
        
        if char["name"] == name:
            print(f'{name} esta en la cola y es {char["superhero"]}')
            
        queue.arrive(char)
        
print('F) Identificar si Carol Danvers esta en la cola')
serch_character(queue,'Carol Danvers')
