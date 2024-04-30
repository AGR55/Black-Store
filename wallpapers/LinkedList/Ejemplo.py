from List import ListNode
from Libro import Libro

lista = ListNode()

libro1 = Libro("Pepe en la casa blanca", "Adriano", "B7345")
libro2 = Libro("Los espejuelos de Paula", "Mariano", "M2389")
libro3 = Libro("Mauricio el cascarrabias", "Dora", "M2379")
libro4 = Libro("El rincon de Pedrito", "Jesse", "H2396")
libro5 = Libro("Asalto en Cienfuegos", "Ana Rosa", "O8937")
libro6 = Libro("Programacion momentanea", "Frank", "P9230")
libro7 = Libro("Indiana Jones", "Pepito", "O2304")
libro8 = Libro("La vida es una fritura", "Pancracio", "G1234")

libro = [libro1, libro2, libro3, libro4, libro5, libro6, libro7]

for i in libro:
    lista.append(i)

lista.insert(3, libro8)
lista.delete(3)
pepe = lista.pop()

for i in range(0, len(libro) - 1):
    print(lista.get(i))

print(pepe)
