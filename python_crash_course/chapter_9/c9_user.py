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
            print(f"Welcome, Mrs. {self.first_name} {self.last_name}")

user1 = User("Mohit", "Kumar", 30, "Male")
user2 = User("Harry", "Singh", 19, "Male")
user3 = User("Samriti", "Rani", 22, "Female")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()