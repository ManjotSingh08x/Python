
pizzas = ["peperonni", 'cheese', 'farmhouse', 'chicken', 'pineapple', "spicy", 'special']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really like all kinds of pizzas")
print("the first three items are: ")
print(pizzas[0:3])
print("the middle three items are: ")
print(pizzas[2:5])
print('the last three items are:')
print(pizzas[-3:])

friend_pizzas = pizzas[:]
pizzas.append('mithu special')
friend_pizzas.append('friend special')

print('my favourite pizzas are:')
for pizza in pizzas:
    print(pizza, end=' ')
    
print()

print("my friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza, end=' ')
