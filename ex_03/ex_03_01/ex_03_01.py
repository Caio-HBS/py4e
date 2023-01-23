horas = input('Quantas horas você trabalhou? ')
razao = input('Quanto você ganha por hora? ')

if int(horas) > 40:
    normal = int(horas) * int(razao)
    extra = (int(horas) - 40) * (int(razao) * 0.5)
    horaextra = normal + extra
    print('Resultado:', horaextra)
else:
    print('Resultado:', int(horas) * int(razao))
