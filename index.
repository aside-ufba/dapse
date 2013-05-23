#!/bin/bash
Default=index
Src='https://raw.github.com/timm/dapse/master'

wget -q -O - $Src/index.cgi > tmp1; chmod 755 tmp1;  mv tmp1 index.cgi
wget -q -O - $Src/style.css > style.css

echo "Content-type: text/html"
echo ""

Q=${QUERY_STRING:=$Default}
Q=$(echo $Q | sed 's/[^0-9a-zA-Z]//g')

wget -q -O - $Src/${Q}.rst | 
rst2html  --title "$Q" --stylesheet "style.css"

