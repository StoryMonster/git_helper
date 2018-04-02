import sys
from commitSearcher import search
from conflictSolver import show_conflicts, apply_solutions
from statusScanner import collect_modifications
from help import print_help

VERSION = 'V1.0'


def find(keyword):
    search(keyword)


def apply_conflict():
    apply_solutions()


def read_conflict():
    show_conflicts()


def add_modifications():
    collect_modifications()


if __name__ == '__main__':
    argv, argc = sys.argv, len(sys.argv)
    assert argc >= 2, "githelper need at least 2 options"
    if argv[1] == 'find':
        assert argc == 3, "what to find?"
        find(argv[2])
    elif argv[1] == 'applyconflict':
        assert argc == 2, "extra options are found"
        apply_conflict()
    elif argv[1] == 'readconflict':
        assert argc == 2, "extra options are found"
        read_conflict()
    elif argv[1] == 'status':
        assert argc == 2, "extra options are found"
        add_modifications()
    elif argv[1] == '--help':
        print_help(VERSION)
    else:
        assert False, "unknow options"
