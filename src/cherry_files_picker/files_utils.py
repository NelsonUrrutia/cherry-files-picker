import os
from .cherry_picker_data import (
    get_cherry_picker_data_files,
    set_cherry_picker_data_file,
    get_cherry_picker_data
)
from .helpers import BOLD, ENDBOLD, get_user_input


def validate_file_path(file_path: str):
    """Validates file path"""
    return os.path.exists(file_path)


def continue_file_path_registration():
    u_option = get_user_input(
        "Valid option [y/N]",
        f"\n{BOLD}Would you like to add another files? [y/N]:{ENDBOLD} ",
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
    """Retrieves file"""
    current_working_directory = "./"
    matching_files = []

    file_name = get_user_input("Enter part or all of the file name", f"\n{BOLD}Search for a file:{ENDBOLD} ", True)
    
    selected_files = get_cherry_picker_data_files()
    if len(selected_files) > 0:
        print(f"\n {BOLD}Selected files:{ENDBOLD}")
        for selected in selected_files:
            print(f" > {selected}")
    

    for root, _, files in os.walk(current_working_directory):
        for fname in files:
            if file_name in fname:
                file_obj = {
                    "src": os.path.join(root, fname),
                    "name": fname
                }
                matching_files.append(file_obj)
                
    if not len(matching_files):
        print(f" > No files found matching {BOLD}{file_name}{ENDBOLD}.")
        print("    You can try a shorter or more general name.")
        get_file_path()
        
    
    print(f"\n{BOLD}Matching files found:{ENDBOLD}\n")
    print(f" {BOLD}INDEX{ENDBOLD} {BOLD}FILE NAME{ENDBOLD}\n")
    for i, f in enumerate(matching_files):
        print(f"  [{i}]   {f['name']}")
        print(f"          > Path: {f['src']}\n")
    
    raw_indexes = get_user_input("File index", f"\nSelect file indexes (comma-separated for multiple): ", True)        

    indexes = []
    invalid_indexes = []

    for part in  raw_indexes.split(","):
        part = part.strip()
        if part.isdigit():
            indexes.append(int(part))

    for index in indexes:
        if  index < len(matching_files):
            selected = matching_files[index]
            print(f" > Added: {selected['name']}")
            set_cherry_picker_data_file(selected["src"])
        else:
            invalid_indexes.append(f"{index}")

    if len(invalid_indexes) > 0:
        print(f"Invalid index(es): {", ".join(invalid_indexes)}")

    if continue_file_path_registration():
        return get_file_path()
    
    print(get_cherry_picker_data("files"))

    
    # file_name = get_user_input("File name", f"\n{BOLD}File name:{ENDBOLD} ", True)
    # valid_file_path = validate_file_path(file_path)
    # if valid_file_path:
    #     set_cherry_picker_data_file(file_path)
    #     print(f" > File path {BOLD}{file_path}{ENDBOLD} registered")
    #     continue_registration = continue_file_path_registration()
    #     if continue_registration:
    #         get_file_path()
    # else:
    #     print(f" > File path {BOLD}{file_path}{ENDBOLD} doesn't exists")
    #     print(f"   Did not register {BOLD}{file_path}{ENDBOLD}")
    #     continue_registration = continue_file_path_registration()
    #     if continue_registration:
    #         get_file_path()


def init_files_utils():
    """Initialize Files utils module"""
    print(f"\n--{BOLD}2. FILES SETTINGS{ENDBOLD} --\n")
    print(" • Register the files path to merge")
    get_file_path()
