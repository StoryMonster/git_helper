import os


def print_operators(files_to_add, files_to_remove, untracked_files):
    print('\n\n\n\n')
    for file in files_to_add:
        print("git add {}".format(file))
    for file in files_to_remove:
        print("git rm {}".format(file))
    print("\n===Below are untracked files===")
    if len(untracked_files) == 0:
        print('<None>\n')
        return
    for file in untracked_files:
        print("git add {}".format(file))
    print('\n\n')


def get_file_from_line(line):
    lst = line.split()
    for item in lst:
        if os.path.exists(item):
            return item

            
def collect_modifications():
    act_tracked = True
    files_to_add = list()
    files_to_remove = list()
    untracked_files = list()
    while True:
        try:
            line = input()
            print(line)
        except EOFError:
            print_operators(files_to_add, files_to_remove, untracked_files)
            break
        if act_tracked:
            if line.find("modified:") != -1:
                files_to_add.append(get_file_from_line(line))
            elif line.find("deleted:") != -1:
                files_to_remove.append(get_file_from_line(line))
            elif line.find("Untracked files:") != -1:
                act_tracked = False
        else:
            file = get_file_from_line(line)
            if file:
                untracked_files.append(file);