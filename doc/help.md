**commitOffset**
Sometimes, you may get a commit id, but maybe this commit is very old, and if you want to check what this commit did, it may be difficult for ypu to look through all git logs.

But with this commitOffset, you can input any exist commit id, and specify how many commit before this commit to compare with, you can get that commit id, then use git diff you can check what's the modification of the specific commit id.

'''
git log | commitOffset -n commit_id
# n is number of commits before commit_id
# commid_id is the commit you want to check
# the output is the commit id before commit_id n times 
'''

**commitSearcher**
You want to get some commit information from git logs, but you just know a keyword. So your choice maybe "git log | grep keyword", but this shall disappoint you, since it will appear only one line contains your keyword.
Below command shall cheer you up, since it will appear entire commit information.
'''
git log | commitSearcher keyword
'''

**conflictSolver**
You must ever met such situation, a big project with thousands files, you use "git pull --rebase", and git notice you there are hunderds of files need to solve conflicts, in such scenario, you may need a noodle to kill yourself.
But, with below command, you will get all conflicts in one file named conflicts.txt.
'''
git pull --rebase | conflictSolver
'''
After solve all conflicts in the file conflicts.txt, just use below command to apply modification to your project.
'''
conflictSolver --apply conflicts.txt
git add <all conflict files>
git rebase --continue
'''
