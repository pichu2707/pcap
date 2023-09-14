from Revista import Revista
from Libro import Libro

libro1 = Libro("L1_123", "La Bestia", "9788408249849")
print("Mi primer libro es:" , libro1)
print("Número ejemplares totales:", libro1.num_totales)
print("Número libros totales:", libro1.num_libros_totales)
print("Número ejemplares prestados:", libro1.num_prestados, "\n")


libro2 = Libro("L2_345", "últimos días en Berlín", "9788408249856")
print("Mi segundo libro es:" , libro2)
print("Número ejemplares totales:", libro1.num_totales)
print("Número libros totales:", libro1.num_libros_totales)
print("Número ejemplares prestados:", libro1.num_prestados, "\n")


revista1 = Revista("R1_JDJ", "National Geographic", "5")
print("Mi primera revista es:", revista1)
print("Número ejemplares totales:", revista1.num_totales)
print("Número revistas totales:", revista1.num_revistas_totales)
print("Número ejemplares prestados:", revista1.num_prestados, "\n")


revista2 = Revista("R2_ADA", "National Geographic", "23")
print("Mi segunda revista es:" , revista2)
print("Número ejemplares totales:", revista1.num_totales)
print("Número revistas totales:", revista1.num_revistas_totales)
print("Número ejemplares prestados:", revista1.num_prestados, "\n")


revista1.prestar()
libro1.prestar()


print("Número ejemplares prestados:", libro1.num_prestados) 

libro1.devolver()

print("Número ejemplares prestados:", libro1.num_prestados, "\n")


'''
1º) C
Dará el error por intentar acceder a la instancia del padre desde el hijo
2º) C, F, J y H
Dará un erro accediendo a la variable desde la instancia en lugar de getters
además devolverá el error por no tener atributo c
3º)F
Inicializar la clase padre
4º) True es el resultado que nos ofrecería
'''