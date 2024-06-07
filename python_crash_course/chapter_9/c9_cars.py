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
        
    
my_used_car = Car('Sabaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.update_odometer(3333)
my_used_car.read_odometer()