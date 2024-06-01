prompt = 'Enter your age for ticket price'
prompt += '\n(Type 0 to quit program): '

#conditional version
# age = None
# while age != 0:
#     age = int(input(prompt))
#     if age != 0:
#         if age < 3:
#             print('The ticket is free!')
#         elif age >=3 and age < 12:
#             print('The price of ticket is $10')
#         elif age >= 12:
#             print('The price of ticket is $15')
#         print('\nNext customer!\n')
#     else:
#         print('exiting the program...')
        
# #active version
# active = True
# while active:
#     age = int(input(prompt))
#     if age == 0:
#         print('exiting the program...')
#         active = False
#     else:
#         if age < 3:
#             print('The ticket is free!')
#         elif age >=3 and age < 12:
#             print('The price of ticket is $10')
#         elif age >= 12:
#             print('The price of ticket is $15')
#         print('\nNext customer!\n')

# #break version
while True:
    age = int(input(prompt))
    if age == 0:
        print('exiting the program...')
        break
    if age < 3:
        print('The ticket is free!')
    elif age >=3 and age < 12:
        print('The price of ticket is $10')
    elif age >= 12:
        print('The price of ticket is $15')
    print('\nNext customer!\n')