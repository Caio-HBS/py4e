han = open('mbox-short.txt')
count = 0
value = 0

for line in han :
    line = line.strip()
    words = line.split()
    if len(words) < 2 :
        continue
    if words[0] == 'X-DSPAM-Confidence:' :
        count = count + 1
        number = float(words[1])
        value = value + number
    else :
        continue
print(value/count)
