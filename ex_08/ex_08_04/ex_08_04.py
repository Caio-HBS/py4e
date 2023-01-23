inp = input('Enter a file name: ')
handle = open(inp)
listapalavras = list()

for line in handle :
    line = line.rstrip()
    words = line.split()
    # listapalavras += words
    for x in words :
        if x in listapalavras :
            continue
        listapalavras.append(x)

listapalavras.sort()
print(listapalavras)
