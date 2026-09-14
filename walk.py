import os


def print_hierarchy(root_dir, exclude_dirs=None):
    """
    Walks through directories and prints a visual tree hierarchy.
    Skips any directories specified in the exclude_dirs list.
    """
    if exclude_dirs is None:
        exclude_dirs = [".venv", ".git"]

    # Normalize paths to handle trailing slashes correctly
    root_dir = os.path.abspath(root_dir)
    print(f"📁 {os.path.basename(root_dir)}")

    for root, dirs, files in os.walk(root_dir):
        # Modifying dirs in-place tells os.walk to skip those directories
        # Using a list comprehension ensures we filter out all matching folders
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # Calculate the current depth level to manage indentation
        level = root.replace(root_dir, '').count(os.sep)
        indent = '   ' * level
        sub_indent = '   ' * (level + 1)

        # Print current directory name (except for the root directory itself)
        if root != root_dir:
            print(f"{indent}📁 {os.path.basename(root)}")

        # Print all files in the current directory
        for file in files:
            print(f"{sub_indent}📄 {file}")


if __name__ == "__main__":
    # Change '.' to a specific folder path if you want to scan somewhere else
    target_directory = "."

    # Pass the folders you want to exclude
    folders_to_skip = [".venv", ".git", ".idea"]

    print_hierarchy(target_directory, exclude_dirs=folders_to_skip)
