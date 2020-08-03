#!/bin/bash

for folder in {1..50}
do
	mkdir $folder
	cd $folder
	for file in {1..30}
	do
		touch maybe_here_$file
		chmod 000 maybe_here_$file
	done
	cd ..
done

cd 32
echo "flag{you_got_the_flag}" > maybe_here_13
chmod 444 maybe_here_13
