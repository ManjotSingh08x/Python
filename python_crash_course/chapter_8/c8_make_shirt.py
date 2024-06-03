def make_shirt(size='large', message='I love Python'):
    print(f'The size of shirt is {size} and the message printed is:\n{message}')
    
make_shirt('small', 'Python is op')
make_shirt(message='python is too op', size='large')
make_shirt()

def describe_city(city, country="India"):
    print(f'{city.title()} is in {country.title()}')
    
describe_city('Delhi')
