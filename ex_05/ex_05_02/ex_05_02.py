num = 0
tot = 0.0
lista_total = list()

while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue
    lista_total.append(fval)

# print('ALL DONE!')
print('Valor máximo:',max(lista_total),'Valor Mínimo:',min(lista_total))
