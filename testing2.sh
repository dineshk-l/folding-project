#!/bin/bash
for value in {1..2}
	do
		gen=$(cat elementary_tests/$value.in | python3 main.py)
		exp=$(cat elementary_tests/$value.out)
		if [ "$gen" != "$exp" ]; then
			echo "Test case $value doesn't work. Expected: $exp ; Generated: $gen ";
		fi
	done