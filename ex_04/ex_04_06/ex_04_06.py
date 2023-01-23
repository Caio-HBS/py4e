def computepay(ih, ir):
    if int(ih) > 40:
        normal = int(ih) * int(ir)
        extra = (int(ih) - 40) * (int(ir) * 0.5)
        resultado = normal + extra
    else:
        resultado = int(ih) * int(ir)
    return resultado

ih = input('Quantas horas você trabalhou? ')
ir = input('Quanto você ganha por hora? ')

resul = computepay(ih,ir)

print('Resultado:', resul)
