# ANSI escape code for bold text
BOLD = "\033[1m"
ENDBOLD = "\033[0m"


def get_user_input(label: str, message: str, is_required: bool):
    """Retrieves the user input"""
    user_input = input(f"{message}")
    if is_required and not user_input:
        print(f" > {BOLD}{label}{ENDBOLD} is required")
        get_user_input(label, message, is_required)
    return user_input
