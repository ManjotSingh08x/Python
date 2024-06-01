cities = {
    'Delhi': {
        'country': 'India',
        'population': 32_941_000,
        'fact': 'It is the capital of India'
        },
    'New York': {
        'country': 'USA',
        'population': 8_340_000,
        'fact': 'more than 800 languages are spoken here'
        },
    'Dublin': {
        'country': 'Ireland',
        'population': 544_000,
        'fact': 'It was founded by Vikings' 
        }
    }

for name, info in cities.items():
    print(f'\n*The name of city is {name}')
    print(f'*It is situated in {info['country']}')
    print(f'*It has a population of {info['population']}')
    print(f'*An interesting fact about it:\n{info['fact']}')