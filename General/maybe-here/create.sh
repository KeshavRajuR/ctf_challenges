#!/bin/bash

#run the script with SUDO privileges

mkdir maybe_here
cd maybe_here

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
chmod 644 maybe_here_13
echo "flag{1_c4n_f1nd_4ny_f1l3}" > maybe_here_13
chmod 444 maybe_here_13
cd ..

zip -qq -r maybe_here.zip *
chmod 664 maybe_here.zip
mv maybe_here.zip ..
cd ..
rm -r maybe_here
