
# create an empty list

list = []

# ask for grocery items.
# enter 'done' when complete
item = ''

while item != 'done':
    item = input('Put an item on your list: ')
    if item != 'done':
        list.append(item)

print('Time to go shopping!')

while len(list) > 0:
    item = input('what did you put in the cart?  ')
    if item in list:
        list.remove(item)
    else:
        print('you strayed from the List.')

print('Time to Check Out')
