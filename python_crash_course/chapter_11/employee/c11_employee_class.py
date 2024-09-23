class Employee:
    """A class resembling info related to an employee"""
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name 
        self.salary = salary
    
    def give_raise(self, increment=5000):
        self.salary += increment
        
        