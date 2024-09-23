from pathlib import Path 

path = Path('chapter_10/guest_book.txt')
content = ''
while True:
    print("To exit out of the program enter 'q'")
    name = input("Enter your name: ")
    if name == 'q':
        break
    else: 
        content += name 
        content += '\n'

    
path.write_text(content)