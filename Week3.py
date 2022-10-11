from pyexpat.errors import XML_ERROR_BINARY_ENTITY_REF
from re import X

def promptWord(startsWith):
    word = input('give me a word that starts with  ' + startsWith + ': ')
        
    while word.startswith(startsWith) == False:
         print(word + ' does not start with ' + startsWith)
         word = input('give me a word that start with ' + startsWith + ': ')
    return word
    
word = promptWord('x')
print('The winning word is ' + word)

