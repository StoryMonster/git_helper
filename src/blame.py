import os

UNNECCESSARY_FOLDER_OF_FILES = [".git", ".gitignore", ".gitmodules", "hooks", ".", ".."]


def print_matched_files(matched_files):
    print("Matched files:")
    for file in matched_files:
        print("    {}".format(file))
    print("You can use git blame <filename> to continue you operations")


def get_repository_root():
    files = os.listdir(".")
    upper_path = ""
    while ".git" not in files:
        upper_path += "../"
        files = os.listdir(upper_path)
    return os.path.abspath(os.path.join(os.getcwd(), upper_path))


def go_through_the_repository_and_do_file_match(file_name, root):
    files = os.listdir(root)
    if (".git" in files) and (root != os.getcwd()):
        # it's not neccessary to check the files in submodules
        return []
    matched_files = []
    for file in files:
        if file in UNNECCESSARY_FOLDER_OF_FILES: continue
        file_path = os.path.abspath(os.path.join(root, file))
        if os.path.isfile(file_path):
            if file == file_name: matched_files.append(file_path)
        elif os.path.isdir(file_path):
            matched_files_in_subdir = go_through_the_repository_and_do_file_match(file_name, file_path)
            matched_files.extend(matched_files_in_subdir)
    return matched_files


def find_files(file_name):
    repository_root = get_repository_root()
    os.chdir(repository_root)
    return go_through_the_repository_and_do_file_match(file_name, repository_root)


def git_blame(file_name):
    matched_files = find_files(file_name)
    assert len(matched_files) != 0, "Cannot find {}".format(file_name)
    os.system("git blame {}".format(matched_files[0])) if len(matched_files) == 1 else print_matched_files(matched_files)
        