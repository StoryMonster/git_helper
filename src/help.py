

V1_0_desc = """
gitHelper v1.0
author: dochen
date: 2018-04-02

commands:
git log | githelper find <keyword>           # to find entire commit information which contains keyword
git status | githelper status                # to help automatically create "git add / git rm" commands
git pull --rebase | githelper readconflict   # to collect all conflicts, and save in one file, conflicts.txt
git rebase <branch> | githelper readconflict # to collect all conflicts, and save in one file, conflicts.txt
githelper applyconflict                      # to apply your modification about conflicts.txt into project
"""

desc_map = {'V1.0': V1_0_desc}


def print_help(version='V1.0'):
    print(desc_map[version])
