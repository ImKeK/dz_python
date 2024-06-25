import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO)

# Создание объекта namedtuple для хранения информации о файлах и каталогах
FileEntry = namedtuple('FileEntry', ['name', 'extension', 'is_directory', 'parent_directory'])

def process_directory(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            entry = FileEntry(name=directory, extension='', is_directory=True, parent_directory=os.path.basename(root))
            logging.info(f"Directory: {entry}")
        for file in files:
            filename, file_extension = os.path.splitext(file)
            entry = FileEntry(name=filename, extension=file_extension, is_directory=False, parent_directory=os.path.basename(root))
            logging.info(f"File: {entry}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py /path/to/directory")
        sys.exit(1)
    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' is not a directory.")
        sys.exit(1)
    process_directory(directory_path)
