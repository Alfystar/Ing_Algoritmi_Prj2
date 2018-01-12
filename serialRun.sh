#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand2,rand
# arg2= quante volte aumento di 200 il numero di elementi partendo da 200
# arg3= OutFileDir
# arg4= son (se la modalità la prevede ma non chiama errore)

echo eseguo lo script:
#./runAndData.sh  <forma> <output del medio> <nElem> <OutFileDir> <son>

#./runAndData.sh  $1 0 $2 $3 $4

#[["$1" != "fractal"] || ["$1" !="rand2"]]
#if [[$1 != "fractal"] && [$1 !="rand2"]];	then
#		out="son$4Time.dat"
#		echo è frattale o sfilacciato
#	else
#		out="Time.dat"
#		echo non è frattale o sfilacciato
#fi


out="son$4Time.dat"
echo Modalità "$1" > $3/"$1$out" 	#svuoto il file che conterrà i tempi
echo "nElem, Time(s)" >> $3/"$1$out"  	#creo nomi colonne
echo "<#>./serialRun $1 $2 $3 $4">>$3/logAction.log
for i in $(seq $2);
do
	./runAndData.sh  $1 0 $((200*$i)) $3 $4
	echo fatto "$i"
	echo $(date) "iterazione $i" $'\n\t' "./runAndData.sh  $1 0 $((200*$i)) $3 $4">>$3/logAction.log

done
echo ------------------------------------------------------------------------------------------------------->>$3/logAction.log
