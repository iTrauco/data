import os

def create_init_py_in_dirs(start_dir="."):
    """
    Walk through the directory tree from the specified starting directory and create
    an __init__.py file in every directory if it doesn't already exist.

    Args:
    start_dir (str): The directory to start from. Defaults to the current directory.
    """
    for root, dirs, files in os.walk(start_dir):
        # Create __init__.py in the current directory if it doesn't exist
        init_file_path = os.path.join(root, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write("# Automatically created __init__.py\n")
            print(f"Created: {init_file_path}")
        else:
            print(f"Already exists: {init_file_path}")

if __name__ == "__main__":
    create_init_py_in_dirs(".")
