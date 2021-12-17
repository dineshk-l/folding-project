#!/bin/bash
for value in {1..41}
	do
		gen=$(cat test-cases/Folding-samples/elementary-tests/$value.in | python main.py)
		exp=$(cat test-cases/Folding-samples/elementary-tests/$value.out)
		if [ "$gen" != "$exp" ]; then
			echo -e "Test case $value doesn't work. Expected: $exp: Generated: $gen\n";
		fi
	done