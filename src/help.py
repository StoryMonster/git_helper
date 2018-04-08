
help_desc = """
gitHelper v1.1
author: dochen
date: 2018-04-08

commands:
git log | githelper find <keyword>           # to find entire commit information which contains keyword
git status | githelper status                # to help automatically create "git add / git rm" commands
git pull --rebase | githelper readconflict   # to collect all conflicts, and save in one file, conflicts.txt
git rebase <branch> | githelper readconflict # to collect all conflicts, and save in one file, conflicts.txt
githelper applyconflict                      # to apply your modification about conflicts.txt into project
"""


def print_help():
    print(help_desc)
