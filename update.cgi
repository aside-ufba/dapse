#!/bin/bash
Style=techmania
Src='https://raw.github.com/timm/dapse/master'

Files="update.cgi index.cgi header.html footer.html" 
for i in $Files; do
	wget -q -O - $Src/$i > $i
done
chmod 755 index.cgi

echo "Content-type: text/html"
echo ""

date
echo "Updated $Files."

