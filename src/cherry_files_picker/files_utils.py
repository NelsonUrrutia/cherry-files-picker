import os

from .cherry_picker_data import (
    get_cherry_picker_data_files,
    set_cherry_picker_data_file,
)
from .helpers import BOLD, ENDBOLD, get_user_input


def validate_file_path(file_path: str):
    """Validates file path"""
    return os.path.exists(file_path)


def continue_file_path_registration():
    u_option = get_user_input(
        "Valid option [y/N]",
        f"\n{BOLD}Continue registration process? [y/N]:{ENDBOLD} ",
        True,
    )
    if u_option == "y" or u_option.capitalize() == "Y":
        return True

    if u_option == "N" or u_option.lower() == "n":
        return False

    return True


def get_files_content():
    """Retrieves a dictionary with files and content"""
    files_and_content = {}
    for f in get_cherry_picker_data_files():
        with open(f) as file:
            content = file.read()
            files_and_content[f] = content
    return files_and_content


def get_file_path():
    """Retrieves file path"""
    file_path = get_user_input("File path", f"\n{BOLD}File path:{ENDBOLD} ", True)
    valid_file_path = validate_file_path(file_path)
    if valid_file_path:
        set_cherry_picker_data_file(file_path)
        print(f" > File path {BOLD}{file_path}{ENDBOLD} registered")
        continue_registration = continue_file_path_registration()
        if continue_registration:
            get_file_path()
    else:
        print(f" > File path {BOLD}{file_path}{ENDBOLD} doesn't exists")
        print(f"   Did not register {BOLD}{file_path}{ENDBOLD}")
        continue_registration = continue_file_path_registration()
        if continue_registration:
            get_file_path()


def init_files_utils():
    """Initialize Files utils module"""
    print(f"\n--{BOLD}2. FILES SETTINGS{ENDBOLD} --\n")
    print(" • Register the files path to merge")
    get_file_path()
