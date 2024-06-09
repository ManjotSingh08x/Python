from pathlib import Path
import json
path = Path('chapter_10/favourit_number.json')

def retrieve_number(path):
    if path.exists():
        contents = path.read_text()
        favourite_number = json.loads(contents)
        print(f"Your favourite number is {favourite_number}")
    else:
        store_number(path)

def store_number(path):
    favourite_number = int(input("Please enter your favourite number: "))
    contents = json.dumps(favourite_number)
    path.write_text(contents)

if __name__ == '__main__':
    retrieve_number(path)