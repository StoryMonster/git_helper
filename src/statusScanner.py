import os
import re


def match(str):
    patterns_with_types = ((r"^\s+modified:\s+(\S+)$", "modify"),
                           (r"^\s+deleted:\s+(\S+)$", "delete"),
                           (r"^\s+(\S+)$", "untrack"))
    for pattern_with_type in patterns_with_types:
        matched = re.match(pattern_with_type[0], str)
        if matched:
            return matched.group(1), pattern_with_type[1]
    return "", "useless"


def collect_modifications():
    git_status_res = os.popen("git status").readlines()
    for line in git_status_res:
        matched_file, matched_type = match(line)
        if matched_type == "modify":
            print("\033[40;31mgit add {}\033[0m".format(matched_file))
        elif matched_type == "delete":
            print("\033[40;31mgit rm {}\033[0m".format(matched_file))
        elif matched_type == "untrack" and os.path.exists(matched_file):
            print("\033[40;31mgit add {}\033[0m".format(matched_file))
        else:
            print(line.strip('\n'))
