#Ejercicio 5
def romano_a_decimal_rec(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    romano = romano.upper()

    if not romano:
        return 0

    if len(romano) == 1:
        return valores[romano]

    actual = valores[romano[0]]
    siguiente = valores[romano[1]]

    if actual < siguiente:
        return siguiente - actual + romano_a_decimal_rec(romano[2:])
    else:
        return actual + romano_a_decimal_rec(romano[1:])

print(romano_a_decimal_rec("MCMXCIV"))

#Ejercicio 22.

def usar_la_fuerza(mochila, objetos_sacados=0):
    if len(mochila) == 0:
        print("No se encontró el sable de luz.")
        return False, objetos_sacados

    objeto = mochila.pop(0)
    objetos_sacados += 1

    if objeto == "sable de luz":
        print(f"Sable de luz encontrado después de sacar {objetos_sacados} objetos.")
        return True, objetos_sacados
    else:
        return usar_la_fuerza(mochila, objetos_sacados)

mochila_jedi = ["comunicador", "botas", "comida", "sable de luz"]

usar_la_fuerza(mochila_jedi)
