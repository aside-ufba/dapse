all:
	- svn add *
	- svn commit -m stuff
	- wget -q -O - http://dapse.unbox.org/?index > /dev/null
	- wget -q -O - http://dapse.unbox.org/?index > /dev/null
