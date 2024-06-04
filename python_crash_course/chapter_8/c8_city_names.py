def city_country(city: str, country: str) -> str:
    full_address = f'{city.title()}, {country.title()}'
    return full_address

print(city_country('New york', 'america'))
print(city_country('gurdaspur', 'india'))
print(city_country('bankok', 'malasyia'))