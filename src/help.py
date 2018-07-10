
help_desc = """
gitHelper v1.3
author: dochen
date: 2018-07-10

commands:
git log | githelper find <keyword>           # to find entire commit information which contains keyword
git log | githelper find -i <commit id>      # to find entire commit information which commit id is specific
git log | githelper statistic [-si | -sd]    # to show the contributors in the branch, -si means incremental sort by commit amount while -sd means decremental sort by commit amount
git status | githelper status                # to help automatically create "git add / git rm" commands
git pull --rebase | githelper readconflict   # to collect all conflicts, and save in one file, conflicts.txt
git rebase <branch> | githelper readconflict # to collect all conflicts, and save in one file, conflicts.txt
githelper applyconflict                      # to apply your modification about conflicts.txt into project
githelper blame <filename>                   # to help use "git blame <filepath>", githelper just need the filename, while git needs the file path
"""


def print_help():
    print(help_desc)
