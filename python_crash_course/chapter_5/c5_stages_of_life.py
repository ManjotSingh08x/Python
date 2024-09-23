import random
age = random.randint(0,100)
print('at the age of',age)
if age < 2:
    print('person is a baby')
elif age >= 2 and age < 4:
    print('person is a toddler')
elif age >= 4 and age < 13:
    print('person is a kid')
elif age >= 13 and age < 20:
    print('person is a teenager')
elif age >= 20 and age < 65:
    print('person is an adult')
else:
    print('person is an elder')
    