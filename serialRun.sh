#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand2,rand
# arg2= quante volte raddoppio il numero di elementi partendo da 100
# arg3= OutFileDir
# arg4= son (se la modalità la prevede ma non chiama errore)

echo eseguo lo script:
#./runAndData.sh  <forma> <output del medio> <nElem> <OutFileDir> <son>

#./runAndData.sh  $1 0 $2 $3 $4

echo Modalità "$1" > $3/"$1"Time.dat 	#svuoto il file che conterrà i tempi
echo "nElem, Time(s)" >> $3/"$1"Time.dat 	#creo nomi colonne
echo "<#>./serialRun $1 $2 $3 $4">>$3/logAction.log
for i in $(seq $2);
do
	./runAndData.sh  $1 0 $((200*$i)) $3 $4
	echo fatto "$i"
	echo $(date) "iterazione $i" $'\n\t' "./runAndData.sh  $1 0 $((200*$i)) $3 $4">>$3/logAction.log

done
echo ------------------------------------------------------------------------------------------------------->>$3/logAction.log
