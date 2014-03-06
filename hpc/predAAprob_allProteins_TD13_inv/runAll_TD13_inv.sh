#!/bin/bash
resultPath=/home/kwang2/result/aaProb_allProteins_TD13_inv/

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
	#sbatch -o $f.slurmlogp6 find.p6.stupidscript.sh $f &
        fname=$(basename $f)
	resultFile=$resultPath${fname%.pw}".csv"
	#echo $resultFile
	sbatch /home/kwang2/scripts/aaCodonProbPred/hpc/predAAprob_allProteins_TD13_inv/each_TD13_inv.sh $f $resultFile &
done
