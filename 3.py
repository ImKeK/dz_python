import os
import logging
import sys

def get_file_info(file_path):
    try:
        file_name = os.path.basename(file_path)
        file_dir = os.path.dirname(file_path)
        file_extension = os.path.splitext(file_name)[1]
        return (file_dir, file_name, file_extension)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py file_path")
        sys.exit(1)
    file_path = sys.argv[1]
    result = get_file_info(file_path)
    if result:
        print(result)

# Реализовано логирование ошибок, также можем в консоли передавать параметры.
