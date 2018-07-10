import sys
import re
from commitSearcher import search_content_in_commit_info, search_commit_id
from conflictSolver import show_conflicts, apply_solutions
from statusScanner import collect_modifications
from statistics import git_log_statistic
from help import print_help


if __name__ == '__main__':
    argv, argc = sys.argv, len(sys.argv)
    assert argc >= 2, "githelper need at least 2 options"
    if argv[1] == 'find':
        if argv[2] == "-i":
            assert argc == 4, "input the commit id"
            assert len(argv[3]) >= 7, "the length of commit id at least 7"
            assert re.match(r"[a-f0-9]+", argv[3]), "incorrect commit id"
            search_commit_id(argv[3])
        else:
            assert argc == 3, "what to find?"
            search_content_in_commit_info(argv[2])
    elif argv[1] == 'applyconflict':
        assert argc == 2, "extra options are found"
        apply_solutions()
    elif argv[1] == 'readconflict':
        assert argc == 2, "extra options are found"
        show_conflicts()
    elif argv[1] == 'status':
        assert argc == 2, "extra options are found"
        collect_modifications()
    elif argv[1] == 'statistic':
        git_log_statistic(argv[2:])
    elif argv[1] == '--help':
        print_help()
    else:
        assert False, "unknow option for '{}'".format(argv[1])
