import questionary

from .cherry_picker_data import (
    get_cherry_picker_data_files,
    set_cherry_picker_data_file,
)
from .helpers import BOLD, ENDBOLD

def get_files_content():
    """Retrieves a dictionary with files and content"""
    files_and_content = {}
    for f in get_cherry_picker_data_files():
        with open(f) as file:
            content = file.read()
            files_and_content[f] = content
    return files_and_content


def get_file_path():
    """Retrieves file"""
    while True:
        file_path = questionary.path("Select a file").ask()
        if file_path == "END" or file_path == "end":
            break
        set_cherry_picker_data_file(file_path)

def init_files_utils():
    """Initialize Files utils module"""
    print(f"\n--{BOLD}2. FILES SETTINGS{ENDBOLD} --\n")
    print(" • Register the files path to merge")
    print(" • Use TAB to navigate and ENTER to select")
    print(" • Type END or end to stop the selecting process \n")
    get_file_path()
