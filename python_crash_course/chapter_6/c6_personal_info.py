person1 = {
    'first_name': 'George',
    'last_name': 'Bush',
    'age': 69,
    'city': 'Seattle',
    }
person2 = {
    'first_name': 'Barack',
    'last_name': 'Obama',
    'age': 50,
    'city': 'New York',
    }
person3 = {
    'first_name': 'Donald',
    'last_name': 'Trump',
    'age': 60,
    'city': 'Manhattan',
    }
people = {
    'person1': person1,
    'person2': person2,
    'person3': person3,
    }
for person, info in people.items():
    full_name = f'{info['first_name']} {info['last_name']}'
    print(f'\nName of person:  {full_name}')
    print(f'Age of person:   {info['age']}')
    print(f'Current city:    {info['city']}')