#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand,sfilacciato,sfilacciatoRand
# arg2= quante volte aumento di 50 il numero di elementi partendo da 50
# arg3= OutFileDir
# arg4= son (se la modalità la prevede ma non chiama errore)

echo eseguo lo script Serial Run per la forma $1, fino a $((50*$2)) Elementi.
#./runAndData.sh  <forma> <output del medio> <nElem> <OutFileDir> <son> <outDircProfile>
#MEMO  ./runAndData.sh  $1 0 $2 $3 $4


#!!! Modifico la variabile Out al fine di rendere più leggibile la funzione
if ( [ $1 != "fractal" ] && [ $1 != "sfilacciato" ] && [ $1 != "sfilacciatoRand" ] && [ $1 != "asterisco" ] );
then
	out="Time.dat"
	echo non è frattale o sfilacciato
	echo Modalità "$1" > $3/"$1$out" 	#svuoto il file che conterrà i tempi, senza i figli

else
	out="Son$4_Time.dat"
	echo è frattale o sfilacciato
	echo Modalità "$1" com $4 son > $3/"$1$out" 	#svuoto il file che conterrà i tempi
fi


echo "nElem, Time(s)" >> $3/"$1$out"  	#creo nomi colonne
echo "<#>./serialRun $1 $2 $3 $4">>$3/logAction.log

#iterazione per migliorare inizio logaritmico
for i in $(seq 4);
do
	nElem=$((10*$i))
	if [[ $nElem == 0 ]];
	then
		nElem=1
	fi
	./runAndData.sh  $1 0 $nElem $3 $4 $out
	echo fatto "dei primi 5 fatto il $i°"
	echo $(date) "iterazione $i" $'\n\t' "./runAndData.sh  $1 0 $nElem $3 $4">>$3/logAction.log
	sleep 0.2	#da tempo a python di essere eliminato da ram
done


for i in $(seq $2);
do
	nElem=$((50*$i))
	./runAndData.sh  $1 0 $nElem $3 $4 $out
	echo fatto "$i°"
	echo $(date) "iterazione $i" $'\n\t' "./runAndData.sh  $1 0 $nElem $3 $4">>$3/logAction.log
	sleep 0.2	#da tempo a python di essere eliminato da ram
done
echo ------------------------------------------------------------------------------------------------------->>$3/logAction.log


