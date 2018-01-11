#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand2,rand
# arg2= quante volte raddoppio il numero di elementi partendo da 100
# arg3= OutFileDir
# arg4= son (se la modalità la prevede ma non chiama errore)

echo eseguo lo script:
#./runAndData.sh  <forma> <output del medio> <nElem> <OutFileDir> <son>

#./runAndData.sh  $1 0 $2 $3 $4

echo Modalità "$1" > $3/"$1"Time.t 	#svuoto il file che conterrà i tempi
for i in $(seq $2);
do
	./runAndData.sh  $1 0 $((100*$((2**$i)))) $3 $4
	echo fatto "$i"
done
