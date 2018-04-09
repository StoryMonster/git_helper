from collections import namedtuple
import operator


Commit = namedtuple('Commit', ['author', 'id', 'date'])   # store commit information for future use
total_commit_counter = 0
result = dict()


def update_result(author):
    global total_commit_counter, result
    total_commit_counter += 1
    if author in result:
        result[author] += 1
    else:
        result[author] = 1


def show_result(authors):
    global total_commit_counter, result
    print("Number of commits in this branch: {}".format(total_commit_counter))
    print("Number of contributed contributors in this branch: {}\n".format(len(result)))
    rank_counter = 0
    for author in authors:
        rank_counter += 1
        print("{}: {} with {} commits".format(rank_counter, author, result[author]))


def sort(reverse=False):
    global result
    authors = list(result)
    authors.sort(reverse=reverse, key=lambda x: result[x])
    return authors


def git_log_statistic(argv):
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.find('Author: ') != -1:
            update_result(line[8:])
    if len(argv) == 0:
        global result
        show_result(list(result))
    for arg in argv:
        if arg == "-si":     # sort incremental by commits amount
            show_result(sort(reverse=False))
        elif arg == "-sd":   # sort decremental by commits amount
            show_result(sort(reverse=True))
        else:
            print("unknow option for '{}'".format(arg))
