#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 packagetoinstall"
    exit 1
fi

trap "echo Do not interrupt!" SIGINT SIGTERM

yum install $1 << EOF
y
EOF


