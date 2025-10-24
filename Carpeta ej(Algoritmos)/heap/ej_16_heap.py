"""16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

from heap import HeapMax

cola_impresion = HeapMax()

#A cargue tres documentos de empleados (cada documento se representa solamente con un nombre
cola_impresion.arrive("Documento_E1", 1)
cola_impresion.arrive("Documento_E2", 1)
cola_impresion.arrive("Documento_E3", 1)

#B imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print("b) Primer documento impreso:", cola_impresion.attention()[1])

#C cargue dos documentos del staff de TI.
cola_impresion.arrive("Documento_TI1", 2)
cola_impresion.arrive("Documento_TI2", 2)

#D cargue un documento del gerente.
cola_impresion.arrive("Documento_G1", 3)

#E imprima los dos primeros documentos de la cola.
print("e) Primer documento impreso:", cola_impresion.attention()[1])
print("e) Segundo documento impreso:", cola_impresion.attention()[1])

#F cargue dos documentos de empleados y uno de gerente.
cola_impresion.arrive("Documento_E4", 1)
cola_impresion.arrive("Documento_E5", 1)
cola_impresion.arrive("Documento_G2", 3)

#G imprima todos los documentos de la cola de impresión.
print("g) Impresión final de todos los documentos pendientes:")
while cola_impresion.size() > 0:
    print("-", cola_impresion.attention()[1])
