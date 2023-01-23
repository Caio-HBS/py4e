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
        counts[wds[1]] = counts.get(wds[1], 0) + 1
temp_list = list()
for k,v in counts.items():
    newtup = (v,k)
    temp_list.append(newtup)

temp_list = sorted(temp_list, reverse=True)

for v,k in temp_list[0:1] :
    print(k,v)
