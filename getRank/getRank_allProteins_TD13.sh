#!/bin/bash
resultPath=/media/work/newData_Feb3_2014/aaProb_allProteins_TD13_rank/

for f in /media/work/newData_Feb3_2014/aaProb_allProteins_TD13/*.csv; do
        fname=$(basename $f)
	resultFile=$resultPath${fname%.csv}"_rank.txt"
	python /home/kuangyu/workspace/aaCodonProbPred/getRank/rankOutput.py $f $resultFile
	#echo $resultFile
done
