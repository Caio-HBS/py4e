#inp_file_name = input('Input file name: ')
#handle = open(inp_file_name)
handle = open('mbox-short.txt')
value = 0
counts = dict()

for line in handle :
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 :
        continue
    if wds[0] != 'From' :
        continue
    if wds[0] == 'From' :
        counts[wds[2]] = counts.get(wds[2], 0) + 1
print(counts)
    #print(dicionario)
