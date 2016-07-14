#!/bin/bash

month=$(echo $(date) | awk '{print $2}')
day=$(echo $(date) | awk '{print $3}' )
if [[ $month == 'Feb' ]];
   then echo "numdays= "$day;
   if [[ $day==29 ]];
   then echo "Leap Year";
   fi;
elif [[ $month == 'Jul' ]];
  then echo "today's day is "$month" "$day;
fi;



