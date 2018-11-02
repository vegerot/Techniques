#!/bin/bash
for file in {data/sp00{20..25}.fits,sp00{18,27}.fits}; do
	fil="$(basename $file)"
	name=${fil#*'_'}
	echo "${name}"
	fitsheader -k "UT" data/$name
done
	
