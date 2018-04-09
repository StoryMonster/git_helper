import sys
from commitSearcher import search
from conflictSolver import show_conflicts, apply_solutions
from statusScanner import collect_modifications
from statistics import git_log_statistic
from help import print_help


if __name__ == '__main__':
    argv, argc = sys.argv, len(sys.argv)
    assert argc >= 2, "githelper need at least 2 options"
    if argv[1] == 'find':
        assert argc == 3, "what to find?"
        search(argv[2])
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
