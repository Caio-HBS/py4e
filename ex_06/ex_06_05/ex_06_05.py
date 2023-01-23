str = 'X-DSPAM-Confidence: 0.8475 '
ponto = str.find('.')
# print(ponto)
espaco = str.find(' ', ponto)
# print(espaco)
num = str[ponto : espaco]
total = float(num)
print(num)
print(total)
