#!/bin/bash                                                                                                                               
FILES=/media/work/newData_Feb3_2014/newData_Feb3_pwNACCESS/*
NOMISPATH='/media/work/newData_Feb3_2014/newData_Feb3_pwNACCESS_noMismatch/'
MISPATH='/media/work/newData_Feb3_2014/newData_Feb3_pwNACCESS_mismatch/'
NOMIS='_noMismatch.pw'
MIS='_mismatch.pw'

for f in $FILES
do
    b=$(basename $f)
    prefix=${b%.*}
    outfile=$NOMISPATH$prefix$NOMIS
    misfile=$MISPATH$prefix$MIS
    python /home/kuangyu/workspace/aaCodonProbPred/preprocessingData/pw_rmMismatch.py $f $outfile $misfile
done


