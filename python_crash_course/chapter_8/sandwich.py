def make_sandwich(*ingredients):
    """Makes a list of ingredients to be added to sandwich and displays it"""
    print('Your sandwich has following ingredients:')
    for ingredient in ingredients:
        print(f'- {ingredient}')