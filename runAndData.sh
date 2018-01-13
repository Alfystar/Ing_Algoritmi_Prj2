#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand2,rand
# arg2= 1/0 (output medio)
# arg3= nElem
# arg4= OutFileDir
# arg5= son (se la modalità la prevede ma non chiama errore)
# arg6= dove piazzare i file del cProfile


if [[ -d $4 ]];then
	echo già esistente $4
else
	echo creo la cartella $4
	mkdir $4	#creo la cartella dove verranno salvati i OutFileDir
fi

if [[ -d $4/cProfile ]];then
	echo "già esistente ./cProfile"
else
	echo "creo ./cProfile"
	mkdir $4/cProfile	#creo la cartella dove verranno salvati i OutFileDir
fi

echo  "parametri passati: ""nElem=" $3 " sonNumber="$5 " OutDir=" $4" OuputData=" $2 " Modalità=" $1 "Dati in uscita su:" $6;
#python3 -m cProfile -o <output cProfile> demoMain.py <modalità> <OutputResul> <nElement> <son>

#!!! Modifico la variabile Out al fine di rendere più leggibile la funzione
out=$6

dirProf="$1x$3elemx$5son"
if [[ -d $4/cProfile/$dirProf ]];then
	echo già esistente
else
	echo creo la cartella $dirProf
	mkdir $4/cProfile/$dirProf
fi

python3 -m cProfile -o $4/cProfile/$dirProf/"$1x$3x$5"elemTest.o demoMain.py $1 $2 $3 $5 >> $4/"$1$out"	#creo tanti cProfile diversi, ma 1 soo file con i tempi
echo progamma eseguito
python3 profileShow.py $4/cProfile/$dirProf/"$1x$3x$5"elemTest.o cumtime > $4/cProfile/$dirProf/"$1x$3x$5"elemTest.dat
