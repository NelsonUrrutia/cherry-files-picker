import subprocess
import questionary

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
    branch = (questionary.select(f"Select the {branch} branch.", choices=branches ).ask())
    set_cherry_picker_data(handle, branch)

def init_branch_utils():
    """Initialize Git Branch module"""
    print(f"\n-- {BOLD}1. BRANCH SETTINGS{BOLD} --\n")
    
    # display_available_branches()

    select_branch("Source","source_branch")

    select_branch("Target","target_branch")

