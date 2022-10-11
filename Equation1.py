from random import randrange

x = randrange(10)
y = randrange(10)
op = randrange(5) # +, -, * , /, %

if op == 0:
    userans = input('What is ' + str(x) + ' x ' + str(y) + '? ')
    ans = x+y
elif: op == 1:
    userans = input('What is ' + str(x) + ' x ' + str(y) + '? ')
    ans = x-y
elif: op == 2:
    userans = input('What is ' + str(x) + ' x ' + str(y) + '? ')
    ans = x*y
elif: op == 3:
    userans = input('What is ' + str(x) + ' x ' + str(y) + '? ')
    ans = x/y
elif: op == 4:
    userans = input('What is ' + str(x) + ' x ' + str(y) + '? ')
    ans = x%y
if:
    int(userans) == ans: :
    print('Nice Work')
else:
    print('Sorry, the correct Answer is ' + str(x+y))

else:
    print('Sorry, the correct Answer is ' + str(x-y))

else:
    print('Sorry, the correct Answer is ' + str(x*y))
else:
    print('Sorry, the correct Answer is ' + str(x/y))
else:
    print('Sorry, the correct Answer is ' + str(x%y))