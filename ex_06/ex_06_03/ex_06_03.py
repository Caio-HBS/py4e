str = input('Input a word: ')
let = input('Input a letter: ')

def count(str,let) :
    word = str
    count = 0
    for letter in word:
        if letter == let :
            count = count + 1
    return count

resul = count(str,let)
print('Input:',str)
print('Letter:',let)
print('Total letters in input:',resul)
