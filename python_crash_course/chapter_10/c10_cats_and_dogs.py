from pathlib import Path

"""print the contents of both files
do a file not found error implementation
print friendly message if not found
make another version where the program moves silently"""

name_files = ['cats.txt', 'dogs.txt']
for name_file in name_files:
    try:
        remaining_path = 'chapter_10/'
        path_name = remaining_path + name_file
        path = Path(path_name)
        contents = path.read_text()
        print(contents)
        
    except FileNotFoundError:
        #pass
        print(f'path {path_name} does not exist')
        