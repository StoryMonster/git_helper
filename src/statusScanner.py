

def print_operators(files_to_add, files_to_remove, untracked_files):
    for file in files_to_add:
        print("git add {}".format(file))
    for file in files_to_remove:
        print("git rm {}".format(file))
    print("\n===Below are untracked files===")
    for file in untracked_files:
        print("git add {}".format(file))


def collect_modifications():
    act_tracked = True
    files_to_add = files_to_remove = list()
    untracked_files = list()
    while True:
        try:
            line = input()
        except EOFError:
            print_operators(files_to_add, files_to_remove, untracked_files)
            break
        if act_tracked:
            if line.find("modified:") != -1:
                files_to_add.append(line.split()[-1])
            elif line.find("deleted:") != -1:
                files_to_remove.append(line.split()[-1])
            elif line.find("Untracked files:") != -1:
                act_tracked = False
        else:
            if line.find("        ") != -1:
                untracked_files.append(line.split()[-1]);