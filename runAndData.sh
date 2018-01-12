#!/bin/bash
#argomeni da passare:
# arg1= linear,star,fractal,rand2,rand
# arg2= 1/0 (output medio)
# arg3= nElem
# arg4= OutFileDir
# arg5= son (se la modalità la prevede ma non chiama errore)

echo creo la cartella $4
mkdir $4	#creo la cartella dove verranno salvati i OutFileDir
mkdir $4/cProfile	#creo la cartella dove verranno salvati i OutFileDir

echo  "parametri passati: ""nElem=" $3 " sonNumber="$5 " OutDir=" $4" OuputData=" $2 " Modalità=" $1;
#python3 -m cProfile -o <output cProfile> demoMain.py <modalità> <OutputResul> <nElement> <son>

python3 -m cProfile -o $4/cProfile/"$1"x"$3"elemTest.o demoMain.py $1 $2 $3 $5 >>$4/"$1"Time.dat	#creo tanti cProfile diversi, ma 1 soo file con i tempi
echo progamma eseguito
python3 profileShow.py $4/cProfile/"$1"x"$3"elemTest.o cumtime >$4/cProfile/"$1"x"$3"elemTest.dat
