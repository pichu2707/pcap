from Ejemplar import Ejemplar

class Libro(Ejemplar):
    libros = []
    num_libros_totales = 0

    def __init__(self, codigo, titulo, isbn):
        super().__init__()
        self.prestado = False
        self.codigo = codigo
        self.titulo = titulo
        self.ISBN = isbn
        Libro.num_libros_totales += 1

    def __str__(self):
        return self.codigo + " - " + self.titulo + " - " + self.ISBN

    def prestar(self):
        super().prestar()
        self.prestado = True
        print(str(self.codigo) + ' PRESTADO')

    def devolver(self):
        super().devolver()
        self.prestado = False
        print(str(self.codigo) + ' DEVUELTO')
