from pathlib import Path 

def count_words(path: Path) -> None:
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry, the file {path} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words.')

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
pathstring = 'C:/Users/acer/PCC_3e_all_solutions/chapter_10/exceptions/'

for filename in filenames:
    path = Path(f'{pathstring}{filename}')
    count_words(path)
    