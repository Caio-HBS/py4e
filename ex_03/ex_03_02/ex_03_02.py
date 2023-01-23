horas = input('Quantas horas você trabalhou? ')
razao = input('Quanto você ganha por hora? ')

try:
    ih = int(horas)
    ir = int(razao)
except:
    ih = -1
    print('Erro, apenas valores numéricos são aceitos')
    quit()

if ih > 40:
    normal = ih * ir
    extra = (ih - 40) * (ir * 0.5)
    horaextra = normal + extra
    print('Resultado:', horaextra)
else:
    print('Resultado:', int(horas) * int(razao))
