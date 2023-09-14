try: 
    notas = []
    sobresalientes = []
    excluidas = 0
    stream = open("fichero_texto.txt", 'r')
    for line in stream:
        try:
            nota = float(line)
            if(nota >= 9.0):
                sobresalientes.append(nota)
            notas.append(nota)
        except Exception: 
            excluidas += 1
    
    print('Las notas leídas son:', notas)
    print('Los sobresalientes son:', sobresalientes)
    print('Líneas exluidas:', excluidas)
except Exception:
    print("No se puede abrir el fichero indicado.")