handle = open('mbox-short.txt')
counts = dict()

for line in handle :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 :
         continue
    if words[0] == 'From' :
        hora = words[5].split(':')
        counts[hora[0]] = counts.get(hora[0], 0) + 1

temp_list = list()

for k,v in counts.items() :
    tuple = (k,v)
    temp_list.append(tuple)

temp_list = sorted(temp_list)

for k,v in temp_list :
    print(k,v)
