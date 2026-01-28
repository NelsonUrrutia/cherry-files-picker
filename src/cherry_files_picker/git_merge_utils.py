import os
import subprocess

from .cherry_picker_data import (
    clear_all_data,
    get_cherry_picker_data,
    get_cherry_picker_data_files,
)
from .files_utils import get_files_content
from .helpers import BOLD, ENDBOLD, get_user_input


def merge_files():
    """Runs subprocess fro git commands"""
    # Get files content
    files_and_content = get_files_content()

    # Swtich branch
    subprocess.run(["git", "checkout", f"{get_cherry_picker_data('target_branch')}"])

    # Checking files
    for file_path, file_content in files_and_content.items():
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(file_path, "w") as target_file:
            target_file.write(file_content)

    # Add all files
    subprocess.run(["git", "add", "-A"])

    # Commit changes
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            f"{get_cherry_picker_data('commit_title')}",
            "-m",
            f"{get_cherry_picker_data('commit_description')}",
            "-m",
            f"Source branch: {get_cherry_picker_data('source_branch')}",
        ]
    )

    clear_all_data()


def confirm_merging():
    """Get user confirmation"""
    response = get_user_input(
        "Selecting a valid option [y/N]",
        f"\n{BOLD}Continue merging process? [y/N]:{ENDBOLD} ",
        True,
    )

    if response == "y" or response.upper() == "Y":
        return True

    if response == "N" or response.lower() == "n":
        return False

    confirm_merging()


def init_merging():
    """Initialize merging process"""
    continue_merging = confirm_merging()
    if not continue_merging:
        print("Merging cancelled")
        return

    merge_files()


def show_summary():
    """Shows data summary"""
    print("\n-- {BOLD}5. SUMMARY{ENDBOLD} --\n")

    print(f"{BOLD}BRANCH SETTINGS{ENDBOLD}")
    print(f" • Source branch: {get_cherry_picker_data('source_branch')}")
    print(f" • Target branch: {get_cherry_picker_data('target_branch')}")

    print(f"\n{BOLD}COMMIT SETTINGS{ENDBOLD}")
    print(f" • Commit title: {get_cherry_picker_data('commit_title')}")
    print(f" • Commit description: {get_cherry_picker_data('commit_description')}")

    print(f"\n{BOLD}FILE SETTINGS{ENDBOLD}")
    for f in get_cherry_picker_data_files():
        print(f" • {f}")


def init_git_merge_module():
    """Initialize git merge utils module"""
    show_summary()
    init_merging()
