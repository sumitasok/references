# https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands
# remove files bulk
find . -name "right*" -print0 | xargs -0 rm

for f in *.pdf; do rm "$f"; done
