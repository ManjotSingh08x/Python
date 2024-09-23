
class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts
    
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
    
    def increment_login_attempts(self, increment=1):
        self.login_attempts += increment
    
    def reset_login_attempts(self):
        self.login_attempts = 0 
    
    def display_login_attempts(self):
        print(f"you have tried to login {self.login_attempts} times.")
        
class Privileges:
    def __init__(self, privileges: list) -> None:
        self.privileges = privileges
        
    def show_privileges(self):
        print("These are the privileges of the Admin:")
        for privilege in self.privileges:
            print(f'- {privilege}')
        
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, login_attempts=0) -> None:
        super().__init__(first_name, last_name, age, gender, login_attempts)
        self.privileges = Privileges([
            'can add post',
            'can delete post',
            'can ban user',
        ])
        

    
    
user1 = Admin("Mohit", "Kumar", 30, "Male")
user2 = User("Harry", "Singh", 19, "Male")
user3 = User("Samriti", "Rani", 22, "Female")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.increment_login_attempts()
user1.display_login_attempts()
user1.increment_login_attempts(4)
user1.display_login_attempts()
user1.reset_login_attempts()
user1.display_login_attempts()

user1.privileges.show_privileges()