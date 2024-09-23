#Rental car section
rental_car = input('What kind of rental car would you like? ')
print(f'Let me see if I can find you a {rental_car.title()}')

#Restaurant settings
number_of_guests = int(input('How many people are in your dinner group? '))
if number_of_guests > 8:
    print('Sorry but you will have to wait for a bigger table')
else:
    print('Your table is ready!')

#Multiples of 10 section
number = int(input('enter a multiple of 10: '))
if number % 10 == 0:
    print('Yes it is a multiple of 10')
else:
    print('it is not a multiple of 10')