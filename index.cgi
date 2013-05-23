#!/bin/bash
Default=index
Src='https://raw.github.com/timm/dapse/master'

echo "Content-type: text/html"
echo ""

Q=${QUERY_STRING:=$Default}
Q=$(echo $Q | sed 's/[^0-9a-zA-Z]//g')

bash _header.html $Q

wget -q -O - $Src/${Q}.rst | 
rst2html  --title "$Q" --stylesheet "_style.css" |
gawk '^<\/body> {In=0}
      In {print}
      /^<body>/ {In=1}'

cat _footer.html
