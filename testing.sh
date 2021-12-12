#!/bin/bash
for value in {1..41}
	do
		gen=$(cat test_cases/Folding-samples/$value.in | python main.py)
		exp=$(cat test_cases/Folding-samples/$value.out)
		if [ "$gen" != "$exp" ]; then
			echo "Test case $value doesn't work. Expected: $exp ; Generated: $gen ";
		fi
	done