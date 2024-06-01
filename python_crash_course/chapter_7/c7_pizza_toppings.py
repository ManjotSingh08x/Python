prompt = '\nEnter a pizza topping that you want'
prompt += '\n(type "quit" to exit the program): '

active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
        print('\nYour order was finalized')
    else:
        print(f'I will add {toppings} to your pizza')