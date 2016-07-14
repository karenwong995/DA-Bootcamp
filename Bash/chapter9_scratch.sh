#!/bin/bash


if [[ -a /tmp/info ]]; then
    rm /tmp/info
fi

dir=.

while read line; do
    echo -n $line | sed "s/: /:/g" | sed "s/\s\{1,\}/:/g" >> /tmp/info
    echo -n ':' >> /tmp/info

    if [[ $(echo $line | cut -d':' -f1) == 'Modify' ]]; then
	echo -e "" >> /tmp/info
    fi
    
done < <(find $dir -type f | xargs stat | egrep 'File|Size|Modify')
    
#awk '{BEGIN FS=':'} {print $2, $4, 
