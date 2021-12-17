#!/bin/bash
for value in {1..508}
	do
		# gen=$(cat test-cases/Folding-samples/elementary-tests/$value.in | python main.py)
		# exp=$(cat test-cases/Folding-samples/elementary-tests/$value.out)
        $(dos2unix test-cases/Folding-samples/elementary-tests/$value.in)
        $(dos2unix test-cases/Folding-samples/elementary-tests/$value.out)
	done