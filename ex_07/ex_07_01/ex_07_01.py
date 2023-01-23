lc = open('mbox-short.txt')
for file in lc :
    nstrip = file.rstrip()
    uc = nstrip.upper()
    print(uc)
