class Ejemplar: 
    num_totales = 0
    num_prestados = 0

    def __init__(self):
        Ejemplar.num_totales += 1

    def prestar(self):
        Ejemplar.num_prestados += 1
    
    def devolver(self):
        Ejemplar.num_prestados -= 1 