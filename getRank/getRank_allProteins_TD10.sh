#!/bin/bash
resultPath=/home/kwang2/result/aaProb_allProteins_TD10_rank/

for f in /home/kwang2/result/aaProb_allProteins_TD10/*.csv; do
        fname=$(basename $f)
	resultFile=$resultPath${fname%.csv}"_rank.txt"
	python /home/kwang2/scripts/aaCodonProbPred/getRank/rankOutput.py $f $resultFile
	#echo $resultFile
done
