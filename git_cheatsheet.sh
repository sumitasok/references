# https://stackoverflow.com/questions/7099833/how-to-revert-a-merge-commit-thats-already-pushed-to-remote-branch
git revert 8f937c6 -m 1
git revert 8f937c6 -m 2

# commit 8f937c683929b08379097828c8a04350b9b8e183
# Merge: 8989ee0 7c6b236
# Author: Ben James <ben@example.com>
# Date:   Wed Aug 17 22:49:41 2011 +0100

# Merge branch 'gh-pages'

# https://github.com/thoughtbot/til/blob/master/git/grab-a-file-from-another-branch.md
git checkout master model.ipynb

git log --author=sumitasok --since=2017-08-01
# https://stackoverflow.com/questions/822811/showing-which-files-have-changed-between-two-revisions
# Showing which files have changed between two revisions
git diff --name-status master..branchName

# Making git use Sublime Text
# https://gist.github.com/geekmanager/9939cf67598efd409bc7
git config --global core.editor "sublime -n -w"

# https://stackoverflow.com/questions/5308816/how-to-use-git-merge-squash
git checkout master
git merge --squash bugfix
git commit
