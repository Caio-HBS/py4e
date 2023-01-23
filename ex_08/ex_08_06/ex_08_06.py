lista_numeros = list()

while True :
    inp_numeros = input('Fale um número: ')
    try :
        inp_numeros = float(inp_numeros)
        lista_numeros.append(inp_numeros)
    except :
        inp_numeros == 'done'
        # lista_numeros.pop()
        break

print('LISTA:',lista_numeros)
print('Menor:',min(lista_numeros),'Maior:',max(lista_numeros))
