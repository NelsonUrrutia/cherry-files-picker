_cherry_picker_data = {
    "source_branch": "",
    "target_branch": "",
    "files": [],
    "commit_title": "",
    "commit_description": "",
}


def get_cherry_picker_data(key: str):
    """Retrieves a value from the store"""
    return _cherry_picker_data.get(key)


def set_cherry_picker_data(key: str, value):
    """Sets a value in the store"""
    _cherry_picker_data[key] = value


def get_cherry_picker_data_files():
    """Retrieves the files array value"""
    return _cherry_picker_data["files"]


def set_cherry_picker_data_file(file: str):
    """Sets a value in the files array"""
    _cherry_picker_data["files"].append(file)


def get_all_data():
    """Return a copy of all data"""
    return _cherry_picker_data.copy()


def clear_all_data():
    """Clears all stored data"""
    _cherry_picker_data.clear()
