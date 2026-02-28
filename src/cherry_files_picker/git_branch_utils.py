import subprocess
import questionary

from .cherry_picker_data import set_cherry_picker_data
from .helpers import BOLD, ENDBOLD

def get_available_branches():
    """Retrieve a list of available branches from Git."""
    result = subprocess.run(["git", "branch", "--list"], capture_output=True, text=True)
    branches = [line.replace("*", "").strip() for line in result.stdout.splitlines()]
    return  branches
        
def select_branch(branch, handle):
    """Prompt the user to select a branch."""
    branches = get_available_branches()
    branch = (questionary.select(f"Select the {branch} branch.", choices=branches ).ask())
    set_cherry_picker_data(handle, branch)

def init_branch_utils():
    """Initialize Git Branch module"""
    print(f"\n-- {BOLD}1. BRANCH SETTINGS{ENDBOLD} --\n")
    select_branch("Source","source_branch")
    print("\n")
    select_branch("Target","target_branch")

