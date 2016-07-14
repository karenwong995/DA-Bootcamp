#!/bin/bash

if [[ ! -f temp1 ]];
then ls *.sh ~/DA-Bootcamp/BashPractice > temp1
fi;

if [[ ! -f temp2 ]];
then ls /usr/bin | grep '^.a.*$' > temp2
fi;

#delete first 3 lines
sed '1,3d' temp2

#print only lines containing pattern "an"
sed -n '/an/p' temp2

#add 'man pages' before every occurrence of "man"
sed '/man/ \i Man pages ' temp2

#get symbolic links and directories
ls -l | egrep '^(d|l)' | sed -e '/^d/ i\ Directory' -e '/^l/ i\ Link' | rev | cut -d ' ' -f1 | rev

