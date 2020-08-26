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
echo "flag{1_c4n_f1nd_4ny_f1l3}" > maybe_here_13
chmod 444 maybe_here_13
