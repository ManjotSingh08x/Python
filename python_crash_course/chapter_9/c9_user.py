class User:
    def __init__(self, first_name, last_name, age, gender) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print("Here is a summary of the profile:")
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    
    def greet_user(self):
        if self.gender == "Male":
            print(f"Welcome, Mr. {self.first_name} {self.last_name}")
        else:
            print(f"Welcome, Mrs {self.first_name} {self.last_name}")