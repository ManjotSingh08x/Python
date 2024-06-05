def make_sandwich(*ingredients):
    print('Your sandwich has following ingredients:')
    for ingredient in ingredients:
        print(f'- {ingredient}')
        
make_sandwich('bread', 'tomato', 'sauce', 'popcorn')
make_sandwich('bread', 'chicken', 'tomato')
make_sandwich('bread', 'egg', 'sauce', 'potato', 'stuart little', 'creatine')