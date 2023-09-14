from Ejemplar import Ejemplar

class Revista(Ejemplar):
    revistas = []
    num_revistas_totales = 0
    def __init__(self, codigo, titulo, numero):
        super().__init__()
        self.prestado = False
        self.codigo = codigo
        self.titulo = titulo
        self.numero = numero
        Revista.num_revistas_totales += 1
    
    def __str__(self):
        return self.codigo + " - " + self.titulo + " - " + self.numero

    def prestar(self):
        super().prestar()
        self.prestado = True
        print(str(self.codigo) + ' PRESTADO')

    def devolver(self):
        super().devolver()
        self.prestado = False
        print(str(self.codigo) + ' DEVUELTO')