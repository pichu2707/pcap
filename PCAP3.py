clientes = {}
dni = ''
dni = input('Introduce NIF del cliente: ')
while dni != '0':
    if dni not in clientes:
        nombre = input('Introduce el nombre del cliente: ')
        compra = int(input('Introduce valor de la compra del cliente: '))
        puntos = ((compra//6)*5)
        cliente = {'nombre':nombre, 'dni':dni, 'compra':compra, 'puntos':puntos}
        clientes[dni] = cliente

    if dni in clientes:
        if dni in clientes:
            print('DNI:', dni)
            for clave, valor in clientes[dni].items():
                print(clave.title() + ':', valor)
    dni = input('Introduce NIF del cliente: ')

    '''
    1ª) B y F
    Al ser mi_lista2 más larga podemos intuir que las id son diferentes por ser diferentes datos los que
    almacena, con loq ue tiene diferente id
    2ª) C
    El resultado es un float y además es la solución a la cuenta matemática que tenemos dentro del for
    3ª) B y G
    Al final la lista acabará siendo (2,) tendréos qeu las id son diferentes de la primera id y la segunda
    ya que mutamoslos datos que tenemos dentro
    4ª) C
    Con la selección de cada uno de los números de cada array si lo igualamos al primer item (empezando desde cero)
    tenemos que nos da los mismos numero es cada una de las tuplas
    '''