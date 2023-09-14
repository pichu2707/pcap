
sueldo1 =-1
sueldo2 =-1 
while sueldo1 < 0: #or sueldo2 < 0:
    sueldo1 = float(input("Introduzca el salario bruto anual del cónyugue 1: "))
    if sueldo1 < 0:
        print("El sueldo debe ser igual o mayor a 0€")
while sueldo2 < 0:
    sueldo2 = float(input("Introduzca el salario bruto anual del cónyugue 2: "))
    if sueldo2 < 0:
        print("El sueldo debe ser igual o mayor a 0€")

suma = sueldo1+sueldo2
print(f"El salario bruto anual de la pareja es: {suma}")
if(sueldo1 >= 0.0) and (sueldo1<12450.00) or (sueldo2 >= 0.0) and (sueldo2<12450.00):
    irpf = 0.19
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2

    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')
elif (sueldo1 >= 12450.0) and (sueldo1<20200.00) or (sueldo2 >= 12450.0) and (sueldo2<20200.00):
    irpf = 0.24
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2
    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')
elif (sueldo1 >= 20200.0) and (sueldo1<28000.00) or (sueldo2 >= 20200.0) and (sueldo2<28000.00):
    irpf = 0.30
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2

    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')
elif (sueldo1 >= 28000.0) and (sueldo1<35200.00) or (sueldo2 >= 28000.0) and (sueldo2<35200.00):
    irpf = 0.303
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2

    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')
elif (sueldo1 >= 35200.0) and (sueldo1<50000.00) or (sueldo2 >= 35200.0) and (sueldo2<50000.00):
    irpf = 0.371
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2

    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')
elif (sueldo1 >= 50000.0) or (sueldo2 >= 50000.0):
    irpf = 0.372
    total1 = sueldo1-(sueldo1*irpf)
    total2 = sueldo2-(sueldo2*irpf)
    anual = sueldo1+sueldo2
    neto = total1+total2

    print(50*'*')
    print(f'El salario bruto anual de la pareja es: {anual}€')
    print(f'El salario bruto anual de la pareja es: {neto}€')
    print(50*'*')

    '''
    Respuestas:
1ª) C
Tenemos puesto a X como 3 y en la función le decimos que tiene que darnos tres valores
y realizar las cuentas que tenemos en la función.
2ª) D
Nos da un error porque nos falta un argumento para la y
3ª) A
Nos dan los resultados de las funciones, nos da el resto y la x 
4ª) E
Tenemos el resultado de la cuenta matemática 20 que es el valor que le damos a X más la división
de 4 entre 2
    '''