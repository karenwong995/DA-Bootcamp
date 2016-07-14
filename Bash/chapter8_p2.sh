#!/bin/bash

echo -n "Enter your choices for compressing $1: "

cat << COMPRESS
gzip
bzip2
zip

COMPRESS


read compressChoice
echo "chosen $compressChoice"

case $compressChoice in
    gzip|bzip2) $compressChoice $1;;
    zip) $compressChoice $1'.zip' $1;;
    esac
