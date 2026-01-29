from .cherry_picker_data import set_cherry_picker_data
from .helpers import BOLD, ENDBOLD, get_user_input


def get_commit_title():
    """Retrieves commit title"""
    title = get_user_input("Commit title", f"\n{BOLD}Commit Title{ENDBOLD}: ", True)
    set_cherry_picker_data("commit_title", title)


def get_commit_description():
    """Retrieves commit description"""
    description = get_user_input(
        "Commit description", f"\n{BOLD}Commit Description{ENDBOLD}: ", True
    )
    set_cherry_picker_data("commit_description", description)


def init_git_commit_module():
    """Initialize Commit utils module"""
    print(f"\n-- {BOLD}3.COMMIT SETTINGS{ENDBOLD} --\n")
    print(" • Enter commit's title and description")
    get_commit_title()
    get_commit_description()
