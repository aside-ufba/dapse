#!/bin/bash
Default=test
Src='https://raw.github.com/timm/dapse/master'

echo "Content-type: text/html"
echo ""

Q=${QUERY_STRING:=$Default}
Q=$(echo $Q | sed 's/[^0-9a-zA-Z]//g')

bash techmania/header.html $Q

wget -q -O - $Src/${Q} | markdown_py

cat techmania/footer.html
