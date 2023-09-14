
a = []
numeros = input('introduce números separados por espacios: ')

lista = numeros.split(' ')
for i in lista:
    if str.lower(i) != "stop":
        a.append(float(i))
    else:
        break
print(50*'=')
print(f'La lista ordenada es {sorted(a)}')
suma_lista = 0
for j in a:
    suma_lista +=j
print(f'La suma total de la lista es: {suma_lista}')
print(50*'=')

'''
Las respuestas a las preguntas son:
1ª) D
tenemos que nos imprimirá por pantalla: 'abc' que concatena con la repetición dons veces de 'xy'
y luego la repetición tres veces de 'a'
2ª) B
Aquí primero concatenamos un guíon que lo hemos asignado en salida, después de esto tenemos
que por orden invertido muestre las tres letras repetidas dos veces a partir de la "Y"
3ª) D
Ya que no podemos crear un entero de un string y menos cuando marca que tiene decimales
en todo caso deberíamos haber creado el float y del float hacer en int
4ª) B y D
Bueno empezamos con el false ya que al ordenar compara cadena con cadena que tenemos dentro de la lista
con lo que tendríamos primero 'aa' comparado con 'AA'
y por último saldría AA-a... por el orden que le hemos asignado a cada una de las listas.
5º) B
ya que lo que nos dice el código es que ejecute el for del rango 4 en i cuando los numeros sean pares
esto es que cuente del 0 al 3 en este caso y que si no, nos marque como menos que son en cuatro ocasiones
es por este motivo que tenemos estos números y el que tengamos el código en comprensión hace que cree dos
listas
'''