#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand,sfilacciato,sfilacciatoRand
# arg2= 1/0 (output medio)
# arg3= nElem
# arg4= OutFileDir
# arg5= son (se la modalità la prevede ma non chiama errore)
# arg6= dove piazzare i file del cProfile


if [[ -d $4 ]];then		#creo la cartella che contiene tutti i dati
	echo già esistente $4
else
	echo creo la cartella $4
	mkdir $4	#creo la cartella dove verranno salvati i OutFileDir
fi

if [[ -d $4/cProfile ]];then	#creo la cartella dei cProfile
	echo "già esistente ./cProfile"
else
	echo "creo $4/cProfile"
	mkdir $4/cProfile	#creo la prima cartella
fi

dirType="$4/cProfile/$1"

if [[ -d "$4/cProfile/$1" ]];then	#creo le cartelle per tipo
	echo "già esistente $4/cProfile/$1"
else
	echo "creo $4/cProfile/$1"
	mkdir "$4/cProfile/$1"	#creo la cartella dove verranno salvati i OutFileDir
fi


echo "dirType vale $dirType"

echo  "parametri passati: ""nElem=" $3 " sonNumber="$5 " OutDir=" $4" Visualizza OuputData=" $2 " Modalità=" $1 "Dati in uscita su:" $6;
#python3 -m cProfile -o <output cProfile> demoMain.py <modalità> <OutputResul> <nElement> <son>

#!!! Modifico la variabile Out al fine di rendere più leggibile la funzione
out=$6

dirProf="$1_x_$3_elem_x_$5_son"
echo "dirProf vale $dirProf"
if [[ -d $dirType/$dirProf ]];then
	echo già esistente
else
	echo creo la cartella "$dirType/$dirProf"
	mkdir $dirType/$dirProf
fi

python3 -m cProfile -o $dirType/$dirProf/"$dirProf"elemTest.o demoMain.py $1 $2 $3 $5 >> $4/"$1$out"	#creo tanti cProfile diversi, ma 1 soo file con i tempi
echo progamma eseguito
python3 profileShow.py $dirType/$dirProf/"$dirProf"elemTest.o cumtime > $dirType/$dirProf/"$1x$3x$5"elemTest.dat
