#!/bin/bash

while read p; do
  FILENAME=`echo "$p" | cut -d/ -f 2`
  python3 get_das_info.py -d "$p" >> $FILENAME.txt
done <qcd_samples.txt


