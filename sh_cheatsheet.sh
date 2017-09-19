# https://stackoverflow.com/questions/941338/how-to-pass-command-line-arguments-to-a-shell-alias
func jn(){
	jupyter noteboook --port=$1
}

# https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands
# remove files bulk
find . -name "right*" -print0 | xargs -0 rm

for f in *.pdf; do rm "$f"; done
