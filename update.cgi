#!/bin/bash
Src='https://raw.github.com/timm/dapse/master'
Files="update.cgi index.cgi _header.html _footer.html _style.css _parts.rst"

for i in $Files; do
	wget -q -O - $Src/$i > $i
done
chmod 755 index.cgi

echo "Content-type: text/html"
echo ""

date
echo "Updated $Files."

