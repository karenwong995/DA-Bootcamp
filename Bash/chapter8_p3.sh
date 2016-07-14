#!/bin/bash


#script to backup the current directory

if [[ $# -gt 0 ]]; then
    echo "Usage: do not put in any arguments"
    exit 1
fi

dir=.
backupDir=/tmp
if [[ $(df $backupDir | awk '{print $4}' | sed '1d') -lt $(du -d 0 $dir | awk '{print $1}') ]]; then
    echo "Not enough space in /var/backups to backup $(pwd)"
    exit 1
fi

backupFile=$(basename $(pwd))'.tar'
if [[ ! -a $backupDir/$backupFile ]]; then
    echo "Creating a new archive /var/backups/$backupFile"
    tar --listed-incremental=$backupDir/log -cvf $backupDir/$backupFile $dir
   
else

    lastModified=$(stat $backupDir/$backupFile | grep 'Modify' | awk '{print $2}')
    daysAgo= $(( ( $(date +%'s') - $(date -d $lastModified +%'s') )/(60*60*24) ))
    if [[ $daysAgo -gt 10 ]]; then
	echo "Archive file was modifed more than 10 days ago. Doing a full backup"
	tar cvf $backupDir/$backupFile.full.$(date +%Y-%m-%d) $dir
	exit 1
    else

	echo -n "Archive of $dir was modified less than 10 days ago. Full or incremental backup? (enter f or i): "
	read type

	if [[ $type == f ]]; then

	    tar cvf /var/backups/$backupFile $dir.full.$(date +%Y-%m-%d)

	elif [[ $type == i ]]; then

	    tar --listed-incremental=$backupDir/log -cvf $backupDir/$backupFile.$(date +%Y-%m-%d) $dir
	fi
    fi
fi


	     
						 
