#!/bin/bash

echo -n "How old are you? "
read age
if [[ $age -le 17 ]];then
    echo "You have $((18-$age)) years left until you are 18"
else
    echo "Your age is $age"
fi
