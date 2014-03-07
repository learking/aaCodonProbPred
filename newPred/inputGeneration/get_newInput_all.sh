#!/bin/bash                                                                                                                                        
resultPath=/home/kwang2/data/newData_Feb3_newInput/newInput_all/

for f in /home/kwang2/data/newData_Feb3_pwNACCESS_noMismatch/*.pw; do
        fname=$(basename $f)
        resultFile=$resultPath${fname%.pw}".csv"
        python AllPW.py $f $resultFile                                                                                                             
done
