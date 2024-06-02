responses = {}

polling_active = True

while polling_active:
    name = input("\n what is your name? ")
    response = input('which mountain would you like to climb some day? ')
    responses[name] = response
    
    repeat = input('Would you like to let another person respond? (y/n) ')
    if repeat == 'n':
        polling_active = False
        
print('\n---------Polling Results---------')
for name, response in responses.items():
    print(f'{name.title()} would like to climb {response.title()}')