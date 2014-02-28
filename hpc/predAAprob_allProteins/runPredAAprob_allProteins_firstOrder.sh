#!/bin/bash
resultPath=/home/kwang2/result/aaProb_allProteins_firstOrder/

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
	#sbatch -o $f.slurmlogp6 find.p6.stupidscript.sh $f &
        fname=$(basename $f)
	resultFile=$resultPath${fname%.pw}".csv"
	#echo $resultFile
	sbatch -o $fname.slurmlog predAAprob_allProteins_firstOrder.sh $f $resultFile  &
done
