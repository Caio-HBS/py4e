str = input('Input a word: ')
let = input('Input a letter: ')

def count(str,let) :
    string = str
    substring = let
    count = str.count(substring)
    return count
resul = count(str,let)
print('Input:',str)
print('Letter:',let)
print('Total letters in input:',resul)
