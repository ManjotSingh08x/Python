glossary = {
    'print': 'prints the output of the program into the terminal',
    'def': 'used to define a function in python',
    'lists': 'provides the array data structure and is used to store data in linear form',
    'lower()': 'returns a copy of the string with capital letters converted to lowercase',
    }

for key, value in glossary.items():
    print(f'* The meaning of {key}: \n  {value}')

rivers = {
    'nile': 'egypt',
    'krishna': 'india',
    'yellow river': 'china',
    'missisipi': 'united states of america',
    'amazon': 'brazil',
    }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

print('Here is the list of the rivers:')    
for river in rivers.keys():
    print("* " + river.title())

print('Here is the list of the countries:')
for country in rivers.values():
    print("* " + country.title())