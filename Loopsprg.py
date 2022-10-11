user = 'yes'
while user.tolower() == 'yes' or user.tolower() == 'y':
        test = input('please enter a phrase: ')
        alpha = 0
        number = 0
        for c in text:
            if c.isalpha():
                alpha = alpha+1
            if c:isnumberic():
                number = number+1

    print('We looked through  ' + text +  ' and found:  ')
    print(str(alpha) + ' alphabet characters')
    print(str(number) +  ' Numeric Characters ')

    user = input('would you like to enter another phrase? ')
