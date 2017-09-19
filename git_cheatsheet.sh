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
