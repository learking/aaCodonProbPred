#!/bin/bash

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
	#
	#sbatch -o $f.slurmlogp6 find.p6.stupidscript.sh $f &
	echo $f
done
