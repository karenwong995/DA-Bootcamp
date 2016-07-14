#!/bin/bash

echo -e 'display all users who log in with Bash shell \n'
cat /etc/passwd | grep '/bin/bash$' | awk -F: '{print $1}'

echo -e '\n from /etc/group display all lines starting with the string \"daemon\" \n'

cat /etc/group | grep daemon

echo -e "\n print all the lines from the same file that don't contain daemon \n"
cat /etc/group | grep -v daemon

echo -e "\n display localhost information from the /etc/hosts file with line number \n"
cat /etc/hosts | grep -n localhost

echo -e "\n count number of occurrences of localhost \n"
cat /etc/hosts | grep -c localhost

echo -e "\n display a list of /usr/share/doc subdirectories contaning info about shells \n"
ls -d /usr/share/doc/*/ | grep 'shell\|bash'

echo -e "\n number of README files in the above subdirectories \n"
ls -d /usr/share/doc/*/ | grep 'shell\|bash' | xargs ls  | grep -c README

echo -e "\n list of files in home directory modified less than 10 hours ago"
find ~ -maxdepth 1  -mmin -$((10*60))

echo -e "\n alternative way to wc -l using grep \n"
grep -c '^.*$' /etc/group

echo -e "\n check whether a user exists in /etc/passwd \n"
user=dabootcamp
if [[ $(awk -F: '{print $1}' /etc/passwd | grep -c $user) -gt 0 ]]; then
    echo 'user '$user' exists';
fi;



echo -e "\n display config files in /etc that contain numbers in their names \n"
ls /etc | grep [0-9]
