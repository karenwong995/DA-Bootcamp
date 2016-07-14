#!/bin/bash

CONFIG=/var/tmp/sysconfig.out

exec 7<&0
exec < /etc/passwd
read rootpasswd

echo "saving root account info..."
echo "Your root account info: " >> $CONFIG
echo $rootpasswd >> $CONFIG
exec 0<&7 7<&-

echo -n "enter comment or [ENTER] for no comment: "
read comment; echo $comment >> $CONFIG

echo "saving hosts information"

TEMP='/var/tmp/hosts.tmp'
cat /etc/hosts  | grep -v '^#' > $TEMP

exec 7<&0
exec < $TEMP

read ip1 name1 alias1
read ip2 name2 alias2

echo "Your local host configuration: " >> $CONFIG
echo $ip1 $name1 $alias1 >> $CONFIG
echo $ip2 $name2 $alias2 >> $CONFIG



