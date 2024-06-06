class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Our restaurant's name is {self.restaurant_name}.")
        print(f'We serve {self.cuisine_type} cuisine.')
        
    def open_restaurant(self):
        print('The restaurant is now open.')
        
rest1 = Restaurant("Delhi Dhaba", 'Indian')
rest2 = Restaurant("Annapurna", 'Chinese')
rest3 = Restaurant("Mcdonalds", "Italian")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

print(rest1.restaurant_name)
print(rest1.cuisine_type)
rest1.open_restaurant()
