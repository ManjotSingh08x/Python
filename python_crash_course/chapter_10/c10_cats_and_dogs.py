from pathlib import Path

def print_file(path: Path):
    contents = path.read_text(encoding='utf-8')
    print(contents)