

def print_commit(commit_info, prev_commit_id, next_commit_id):
    print("\033[40;33m{}\033[0m".format(commit_info[0]))
    for i in range(1, len(commit_info)):
        print(commit_info[i])
    if prev_commit_id != '':
        print("previous commit: {}".format(prev_commit_id))
    if next_commit_id != '':
        print("next     commit: {}".format(next_commit_id))
    print("")


def search_content_in_commit_info(keyword):
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
                prev_commit_id = line.split()[-1]
                print_commit(commit_info[0:-1], prev_commit_id, next_commit_id)
                prev_commit_id = ''
                act_findout = False
            next_commit_id = commit_info[0].split()[-1]
            commit_info = [line]

            
def search_commit_id(commit_id):
    act_findout, commit_info = False, list()
    prev_commit_id = next_commit_id = ''
    while True:
        try:
            line = input().lower()
        except EOFError:
            if act_findout:
                print_commit(commit_info, prev_commit_id, next_commit_id)
            break
        if line.find("commit ") != -1 and len(line) == 47:
            current_commit_id = line.split()[-1]
            if act_findout:
                prev_commit_id = current_commit_id
                print_commit(commit_info, prev_commit_id, next_commit_id)
                break
            else:
                if current_commit_id.find(commit_id) == 0:
                    act_findout = True
                    commit_info.append(line)
                else:
                    next_commit_id = current_commit_id
        elif act_findout:
            commit_info.append(line)
    