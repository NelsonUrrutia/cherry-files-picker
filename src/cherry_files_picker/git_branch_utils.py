import subprocess

from .cherry_picker_data import set_cherry_picker_data
from .helpers import BOLD, ENDBOLD, get_user_input


def validate_branch(branch):
    """Validate git branch"""
    result = subprocess.run(
        ["git", "rev-parse", "--verify", branch], capture_output=True, text=True
    )

    return result.returncode == 0


def get_source_branch():
    """Retrieves source branch"""
    source_branch = get_user_input(
        "Source branch", f"\n{BOLD}Source branch:{ENDBOLD} ", True
    )
    valid_branch = validate_branch(source_branch)
    if not valid_branch:
        print(f" > Source branch {BOLD}{source_branch}{ENDBOLD} doesn't exist")
        print("   Try again")
        get_source_branch()
        return

    print(f" > Source branch {BOLD}{source_branch}{ENDBOLD} is valid")
    set_cherry_picker_data("source_branch", source_branch)


def get_target_branch():
    """Retrieves target branch"""
    target_branch = get_user_input(
        "Target branch", f"\n{BOLD}Target branch:{ENDBOLD} ", True
    )
    valid_branch = validate_branch(target_branch)
    if not valid_branch:
        print(f" > Target branch {BOLD}{target_branch}{ENDBOLD} doesn't exist")
        print("   Try again")
        get_source_branch()
        return

    print(f" > Target branch {BOLD}{target_branch}{ENDBOLD} is valid")
    set_cherry_picker_data("target_branch", target_branch)


def init_branch_utils():
    """Initialize Git Branch module"""
    print("\n-- {BOLD}1. BRANCH SETTINGS{BOLD} --\n")
    get_source_branch()
    get_target_branch()
