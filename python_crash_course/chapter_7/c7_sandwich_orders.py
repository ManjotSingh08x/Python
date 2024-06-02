sandwich_orders = [
    'pastarami',
    'chicken', 
    'egg',
    'roast beef',
    'pastarami',
    'grilled',
    'cheese',
    'ham',
    'meatball',
    'pastarami'
    ]

finished_sandwiches = []

print('Oops! the Deli has run out of pastarami')
while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)
    
print('\n----Order Summary----\nthese sandwiches were finished:\n ')
for sandwich in finished_sandwiches:
    print('* ' + sandwich)