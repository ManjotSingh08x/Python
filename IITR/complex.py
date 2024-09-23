from math import pow, sqrt
class Complex:
    def __init__(self, a: int, b: int) -> None:
        self.real = a 
        self.imaginary = b
    
def distance(a: Complex, b: Complex):
    return sqrt(pow(a.real - b.real, 2) + pow(a.imaginary - b.imaginary, 2))

def multiply(a: Complex, b: Complex):
    pass
