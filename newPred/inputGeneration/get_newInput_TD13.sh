#!/bin/bash                                                                                                                                        
resultPath=/home/kwang2/data/newData_Feb3_newInput/newInput_TD13/

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
        fname=$(basename $f)
        resultFile=$resultPath${fname%.pw}".csv"
        python AllPW_TD13.py $f $resultFile                                                                                                             
done
