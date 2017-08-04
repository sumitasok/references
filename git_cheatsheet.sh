# Making git use Sublime Text
# https://gist.github.com/geekmanager/9939cf67598efd409bc7
git config --global core.editor "sublime -n -w"

# https://stackoverflow.com/questions/5308816/how-to-use-git-merge-squash
git checkout master
git merge --squash bugfix
git commit
