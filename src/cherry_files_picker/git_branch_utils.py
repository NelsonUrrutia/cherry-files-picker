import subprocess

from .cherry_picker_data import set_cherry_picker_data
from .helpers import BOLD, ENDBOLD, get_user_input

def print_available_branches(branches):
    print(f" {BOLD}INDEX{ENDBOLD}  {BOLD}BRANCH{ENDBOLD}")
    for i, branch in enumerate(branches):
        print(f" [{i}]     {branch}")
        
def get_available_branches():
    result = subprocess.run(["git", "branch", "--list"], capture_output=True, text=True)
    branches = [line.replace("*", "").strip() for line in result.stdout.splitlines()]
    return  branches
    
def validate_branch(branch):
    """Validate git branch"""
    result = subprocess.run(
        ["git", "rev-parse", "--verify", branch], capture_output=True, text=True
    )
    return result.returncode == 0

def get_branch(branch, handle, branches):
    branch_index = get_user_input(f"{branch} index", f"\nSelect the {BOLD}{branch} branch.{ENDBOLD} Use the index: ", True)        

    if not branch_index.isdigit():
        print(f"Please try again with a valid index")
        return get_branch(branch, handle, branches)

    branch_index = int(branch_index)

    if branch_index < 0 or branch_index > len(branches):
        print(f"Please try again with a valid index")
        return get_branch(branch, handle, branches)
    
    branch = branches[branch_index]

    valid_branch = validate_branch(branch)

    if not valid_branch:
        print(f" > Branch {BOLD}{branch}{ENDBOLD} is not valid")
        print("   Try again")
        return get_branch(branch, handle, branches)
    
    print(f" > {BOLD}{branch}{ENDBOLD} selected")
    set_cherry_picker_data(handle, branch)

def init_branch_utils():
    """Initialize Git Branch module"""
    print(f"\n-- {BOLD}1. BRANCH SETTINGS{BOLD} --\n")
    
    branches = get_available_branches()
    
    print_available_branches(branches)

    get_branch("Source","source_branch", branches)

    get_branch("Target","target_branch", branches)

