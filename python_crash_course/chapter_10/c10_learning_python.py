from pathlib import Path

path = Path('chapter_10/learning_python.txt')
contents = path.read_text().rstrip()
contents = contents.replace('Python', 'C++')
print(contents)
for line in contents.splitlines():
    print(line)