prompt = '\nEnter a pizza topping that you want'
prompt += '\n(type "quit" to exit the program): '

#conditional test version
# toppings = ''
# while toppings != 'quit':
#     toppings = input(prompt)
    
#     if toppings != 'quit':
#         print(f'I will add {toppings} to your pizza')
#     else:
#         print(f'\nYour order was finalized')

#active test version
# active = True
# while active:
#     toppings = input(prompt)

#     if toppings == 'quit':
#         active = False
#         print('\nYour order was finalized')
#     else:
#         print(f'I will add {toppings} to your pizza')

#break version
while True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        print(f'\nYour order was finalized')
        break
    else:
        print(f'I will add {toppings} to your pizza')
        
        
    