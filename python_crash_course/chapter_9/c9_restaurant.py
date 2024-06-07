class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"Our restaurant's name is {self.restaurant_name}.")
        print(f'We serve {self.cuisine_type} cuisine.')
        
    def open_restaurant(self):
        print('The restaurant is now open.')
        
    def get_number_served(self):
        print(f"Our restaurant has served {self.number_served} customers.")
    
    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("decreasing number of served customers is not possible")
        
    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print("decreasing number of served customers is not possible")
        
        
rest1 = Restaurant("Delhi Dhaba", 'Indian')
rest2 = Restaurant("Annapurna", 'Chinese')
rest3 = Restaurant("Mcdonalds", "Italian")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

print(rest1.restaurant_name)
print(rest1.cuisine_type)
rest1.open_restaurant()

rest1.get_number_served()

rest1.set_number_served(500)
rest1.get_number_served()

rest1.increment_number_served(150)
rest1.get_number_served()


