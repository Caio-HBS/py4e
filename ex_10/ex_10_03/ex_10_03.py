handle = open('mbox-short.txt')
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
letter_count = dict()

text_as_string = handle.read()

for letter in text_as_string.lower() :
    if letter in alphabet :
        letter_count[letter] = letter_count.get(letter, 0) + 1

temp_list = list()

for k,v in letter_count.items() :
    tuple = (v,k)
    temp_list.append(tuple)

temp_list = sorted(temp_list, reverse=True)

for freq,letter in temp_list :
    print(letter,freq)
