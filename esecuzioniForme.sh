#!/bin/bash
#argomeni da passare:
# arg1= OUTDIR
# arg2= quante ripetizioni

echo esecuzione per il linerare
./serialRun.sh linear $2 $1 100

echo esecuzione per la Stella
./serialRun.sh star $2 $1 100

echo esecuzione per il filoSfilacciato 100 figli
./serialRun.sh rand $2 $1 100

echo esecuzione per il random puro
./serialRun.sh rand2 $2 $1 100

echo esecuzione per il frattale al 2 figli
./serialRun.sh fractal $2 $1 2
