class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year) -> None:
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self) -> str:
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Displays current odometer value"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("rolling back the odometer is not allowed.")
    
    def increment_odometer(self, miles):
        """Add the given amount to odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("rolling back the odometer is not allowed.")
            
class Battery:
    """A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f'This car has a {self.battery_size}-kWh battery.')
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f'This car can go about {range} miles on a full charge')
            
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year) -> None:
        """Initialise attributes of parent class and new attributes of child"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_used_car = Car('Sabaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.update_odometer(3333)
my_used_car.read_odometer()