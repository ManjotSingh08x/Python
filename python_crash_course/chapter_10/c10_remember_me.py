from pathlib import Path
import json 

def get_new_user(path):
    """Prompts for new user info"""
    username = input("What is your name? ")
    age = int(input("what is your age? "))
    gender = input("what is your gender? ")
    user_info = {'username': username, 'age': age, 'gender': gender}
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"we'll remember you when you come back, {username}!")

def user_name_confirmed(user_info: dict):
    """Returns the confirmation that the current user is the person who last ran the program
    if he is isnt, it returns false for resubmision of forms"""
    confirmation = input(f"Is {user_info['username']} your username?(y/n) ")
    if confirmation.lower() == 'y':
        return True
    else:
        return False


def get_stored_user_info(path):
    "Retrieves user info from json file"
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def greet_user(path):
    """greets the user using info stored in json"""
    user_info = get_stored_user_info(path)
    if user_info != None and user_name_confirmed(user_info):
        print(f'Welcome back, {user_info['username']}!')
        print(f"Your age is {user_info['age']}", 
            f"and your gender is {user_info['gender']}")
    else: 
        user_info = get_new_user(path)
        
path = Path('chapter_10/username.json')

if __name__ == '__main__':
    greet_user(path)

    
