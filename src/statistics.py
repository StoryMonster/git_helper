from collections import namedtuple


Commit = namedtuple('Commit', ['author', 'id', 'data'])


def git_log_statistic():
    all_commits = dict()
    commit = list()
    while True:
        try:
            line = input()
        except EOFError:
            if len(commit) > 3 && all_commits.has(Commit(commit[1][8:]):
                all_commits[Commit(commit[1][8:])].append(Commit(commit[1][8:], commit[0][7:], commit[2][8:]))
                commit = []
            break

        if line.find('commit ') != -1 and len(line) == 47:
            if len(commit) > 3 && all_commits.has(Commit(commit[1][8:]):
                all_commits[Commit(commit[1][8:])].append(Commit(commit[1][8:], commit[0][7:], commit[2][8:]))
                commit = [line]

    for author in all_commits:
        print(author + " with " + len(all_commits[author]) + " commits")
