#!/bin/bash

RED='\033[1;31m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Extracting puzzle with password 'password'${NC}\n"

#We first unzip the folder to get the question. Since it is password protected, we'll use the -P option
unzip -qq -P "password" puzzle.zip

mv ./flag/* .
rm -r ./flag

#This variable is used for all the 1000 zip folders present and also for the looping structure
level=999

#Looping structure that will run all the way from 999 to 0, 1000 loops to be executed.
while [ $level -ge 0 ]
do
	echo -e "${YELLOW}---> Extracting level $level${NC}"
	#Processing of pwd.png is done by Python and password is stored into password variable
	password="$(python3 extract-png.py)"

	#Getting the file name
	file_name="flag-"
	file_type=".zip"
	file_fullname="${file_name}${level}${file_type}"

	unzip -qq -P $password "$file_fullname"
	rm "${file_fullname}"
	rm password.png
	
	echo -e "${BLUE}Password used: $password${NC}\n"

	#Unzipping the file and then deleting it
	#Handling the last case where we dont' want the folder to be deleted as it contains our flag.
	if [[ $level -gt 0 ]]
	then
		#Moving files around to arrange them for next iteration
		mv ./flag/* .
		rm -r ./flag
		level=$(( $level - 1 ))
	else
		break
	fi
done

echo -e "${YELLOW}Finished solving the challenge...\nFlag: ${RED}$(cat flag.txt)${NC}\n"
