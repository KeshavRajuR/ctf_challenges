#!/bin/bash

flag="flag{you_got_the_flag}"
level=0

RED='\033[1;31m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo $flag > flag.txt

while [ $level -le 999 ]
do
	echo -e "${YELLOW}--> Creating level $level${NC}"
	if [[ $level -eq 0 ]]
	then
		filename="flag-$level.zip"
		password="$(python3 create-png.py)"
		zip -P $password $filename flag.txt
		mkdir flag
		mv $filename password.png flag/
	else
		filename="flag-$level.zip"
		password="$(python3 create-png.py)"
		zip -r -P $password $filename flag/
		rm -r ./flag
		mkdir flag
		mv $filename password.png flag/
	fi
	echo -e "${BLUE}Password used: $password${NC}"
	level=$(( $level + 1 ))
	echo -e "\n"
done

echo -e "${YELLOW}Creating puzzle.zip with password as 'password'${NC}\n"
zip_password="password"
zip -r -P $zip_password puzzle.zip flag/

echo -e "\n${YELLOW}Deleting flag.txt and other redundant files...${NC}\n"
rm flag.txt
rm -r flag/

echo -e "${YELLOW}Finished creating challenge...\nFlag: ${RED}$flag${NC}\n"
