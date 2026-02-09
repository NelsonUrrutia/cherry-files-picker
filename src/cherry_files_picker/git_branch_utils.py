import subprocess

from .cherry_picker_data import set_cherry_picker_data
from .helpers import BOLD, ENDBOLD, get_user_input


def get_available_branches():
    """Retrieve a list of available branches from Git."""
    result = subprocess.run(["git", "branch", "--list"], capture_output=True, text=True)
    branches = [line.replace("*", "").strip() for line in result.stdout.splitlines()]
    return  branches

def display_available_branches():
    branches = get_available_branches()
    """Display a list of available branches."""
    print(f" {BOLD}INDEX{ENDBOLD}  {BOLD}BRANCH{ENDBOLD}")
    for i, branch in enumerate(branches):
        print(f" [{i}]     {branch}")
        

def validate_branch(branch):
    """Check if a branch exists in Git."""
    result = subprocess.run(
        ["git", "rev-parse", "--verify", branch], capture_output=True, text=True
    )
    return result.returncode == 0

def select_branch(branch, handle):
    """Prompt the user to select a branch."""
    branches = get_available_branches()

    while True:
        try:
            branch_index = int(get_user_input(f"{branch} index", f"\nSelect the {BOLD}{branch} branch.{ENDBOLD} Use the index: ", True))        
            if 0 <= branch_index < len(branches):
                branch = branches[branch_index]
                if validate_branch(branch):
                    print(f" > {BOLD}{branch}{ENDBOLD} selected")
                    set_cherry_picker_data(handle, branch)
                    return
                else:
                    print(" > Branch is not valid. Please try again.")
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please select a number") 

def init_branch_utils():
    """Initialize Git Branch module"""
    print(f"\n-- {BOLD}1. BRANCH SETTINGS{BOLD} --\n")
    
    display_available_branches()

    select_branch("Source","source_branch")

    select_branch("Target","target_branch")

