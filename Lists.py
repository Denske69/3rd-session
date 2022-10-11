from pyexpat import XML_PARAM_ENTITY_PARSING_NEVER


first = ['this', 'is', 'a', 'list']
evens = [2,4,6,8,10]
students = ['abigail', 'ben', 'christi','dave']

# create an empty list
team = []

# ask the user for names.
# enter 'done' when complete
player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

print('your team is: ')
for p in team:
    print("\t" + p)
