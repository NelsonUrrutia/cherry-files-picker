from .files_utils import init_files_utils
from .git_branch_utils import init_branch_utils
from .git_commit_utils import init_git_commit_module
from .git_merge_utils import init_git_merge_module
from .helpers import BOLD, ENDBOLD


def init_cherry_files_picker():
    """
    Initialize tool
    """
    # Print welcome message
    print("\n-------------------------------")
    print(f"- 🍒  {BOLD}Cherry Files Picker{ENDBOLD}  🗂️  - ")
    print("-------------------------------")

    # Get source and target branches
    # init_branch_utils()

    # Get files to merge
    init_files_utils()

    # Get commit message
    # init_git_commit_module()

    # Init merging state
    # init_git_merge_module()
