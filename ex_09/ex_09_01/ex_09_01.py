
input_nome = input('Enter a file name: ')
handle = open(input_nome)
value = 0
dicionario = dict()

for lines in handle :
    lines = lines.rstrip()
    words = lines.split()
    for word in words :
        value = value + 1
        dicionario[word] = value
print(dicionario)
