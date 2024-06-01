favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

invited_peoples = [
    'jen',
    'admin',
    'greg',
    'phil',
    'edward',
    'john',
    'sarah',
    ]
for person in invited_peoples:
    if person in favorite_languages.keys():
        print(f'Thank you {person.title()}, for taking the poll.')
    else:
        print(f'Please take the poll {person.title()}.')