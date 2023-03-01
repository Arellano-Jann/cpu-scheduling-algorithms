batchFile = pa2_batchfile.txt

all:
	make rr
	make srtf
	make bash

rr:
	python3 batchSchedulingComparison.py $(batchFile) RoundRobin

srtf:
	python3 batchSchedulingComparison.py $(batchFile) ShortestRemaining

bash:
	chmod 700 memoryCheck.sh
	./memoryCheck.sh