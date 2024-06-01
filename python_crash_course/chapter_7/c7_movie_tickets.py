prompt = 'Enter your age for ticket price'
prompt += '\n(Type 0 to quit program): '

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