#!/bin/bash
resultPath=/home/kwang2/result/aaProb_allProteins/

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
	#
	#sbatch -o $f.slurmlogp6 find.p6.stupidscript.sh $f &
	resultFile=$resultPath$(f%.pw)".csv"
done
