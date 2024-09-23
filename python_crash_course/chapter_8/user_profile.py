def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

my_profile = build_profile(
    "Manjot",
    'Singh',
    location = 'Punjab',
    qualification = 'educated'
    )

print(my_profile)

def make_car(model_name, manufacturer, **car_info):
    car_info['model_name'] = model_name
    car_info['manufacturer'] = manufacturer
    return car_info

car = make_car(
    'subaru',
    'outback',
    color = 'blue', 
    tow_package = True
    )

print(car)