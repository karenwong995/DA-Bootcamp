#!/bin/bash


echo -n "This script will find the 5 biggest files and the 5 most recently modified files in a directory. Please select directory: "
read dir

while [[ ! -d $dir ]]; do
    echo -n "Not a directory. Please enter a directory"
    read dir
done;

echo "The 5 biggest files are: " 
find $dir -type f | xargs du | sort -n -r -k1 | sed -n '1,5p'

echo "The 5 most recently modified files are: "
find $dir -type f | xargs ls -t | sed -n '1,5p'

