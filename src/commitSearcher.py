import queue

def print_commit(commit_info, prev_commit_id, next_commit_id):
    print("\033[40;33m{}\033[0m".format(commit_info[0]))
    for i in range(1, len(commit_info)):
        print(commit_info[i])
    if prev_commit_id != '':
        print("previous commit: {}".format(prev_commit_id))
    if next_commit_id != '':
        print("next     commit: {}".format(next_commit_id))
    print("")


def search(keyword):
    keyword = keyword.lower()
    act_findout, commit_info = False, list()
    prev_commit_id = next_commit_id = ''
    commit_counter = 0
    while True:
        try:
            line = input().lower()
            commit_info.append(line)
        except EOFError:
            if act_findout:
                print_commit(commit_info, prev_commit_id, next_commit_id)
            break
        if line.find(keyword) != -1: act_findout = True
        if line.find("commit ") != -1 and len(line) == 47:
            commit_counter += 1
            if commit_counter == 1: continue
            if act_findout:
                next_commit_id = line.split()[-1]
                print_commit(commit_info[0:-1], prev_commit_id, next_commit_id)
                next_commit_id = ''
                act_findout = False
            prev_commit_id = commit_info[0].split()[-1]
            commit_info = [line]
