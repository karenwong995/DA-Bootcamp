#!/bin/bash

declare -t variable=2  #what does this do??

#trap "echo I will print variable for every line I debug" DEBUG



set -x
x=$((3+2))
echo $((x+$variable))
echo $variable
set +x


echo "out of debug"


#trap a CTRL-X CTRL-C

trap "echo cannot interrupt!" SIGINT SIGTERM

while true; do
    echo -n "Please enter something: "
    read value
    echo "You entered $value"

    if [[ $value == 'quit' ]]; then
	break
    fi
    
    sleep 5
done
