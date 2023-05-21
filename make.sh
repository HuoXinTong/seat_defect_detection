#!/bin/bash
rm -rf impos.txt pos.txt pos_train impos_train pos.vec
mkdir pos_train impos_train

python -u sample_process.py
python -u description.py

# ./opencv_createsamples.exe -vec pos.vec -info pos.txt -bg impos.txt -num 290 -w 20 -h 20
# ./opencv_traincascade.exe -data data -vec pos.vec -bg impos.txt -numPos 290 -numNeg 510 -numStages 12 -w 20 -h 20 -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -featureType LBP