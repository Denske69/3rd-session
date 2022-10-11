import pprint


def countalpha(t):
    alpha = 0
    for c in t:
        if c.isalpha():
            alpha = alpha+1
    return alpha

def countnumeric(txt):
    number = 0
    for c in txt:
        if c.isnumeric():
            number = number+1
    return number

def countnumeric(ch):
    number = 0
    for c in ch:
        if c.isnumeric():
            count = count + 1
    return number
text = input('please enter a phrase: ')

print('We looked through ' + text + ' and found:')
acount = countalpha(text)
print(str(acount) + ' alphabet characters')
ncount = countnumeric(text)
print(str(ncount) + ' numeric characters')

search = 'yes'
while search.lower() == 'yes':
    ch = input ('What Character would you like to search for? ') 
    count = findchar(text, ch)
    print('we found ' + str(count) + ' of ' + ch +  ' in ' + text + ' . ')
    search = input('Search for another?  ')

