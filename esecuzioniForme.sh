#!/bin/bash
#argomeni da passare:
# arg1= OUTDIR
# arg2= quante ripetizioni di 50 in 50

echo esecuzione per il linerare
./serialRun.sh linear $2 $1 100

echo esecuzione per la Stella
./serialRun.sh star $2 $1 100

echo esecuzione per il filoSfilacciato Deterministico 100 figli
./serialRun.sh sfilacciato $2 $1 100

echo esecuzione per il filoSfilacciato Random 100 figli
./serialRun.sh sfilacciatoRand $2 $1 100

echo esecuzione per il random
./serialRun.sh rand $2 $1 100

echo esecuzione per il frattale al 2 figli
./serialRun.sh fractal $2 $1 2

echo esecuzione per il frattale al 25 figli
./serialRun.sh fractal $2 $1 25

echo esecuzione per il frattale al 100 figli
./serialRun.sh fractal $2 $1 100

echo esecuzione per il frattale al 250 figli
./serialRun.sh fractal $2 $1 250

echo esecuzione per il frattale al 500 figli
./serialRun.sh fractal $2 $1 500

echo esecuzione per lo asterisco a 5 figli
./serialRun.sh asterisk $2 $1 5

echo esecuzione per lo asterisco a 15 figli
./serialRun.sh asterisk $2 $1 15

echo esecuzione per lo asterisco a 40 figli
./serialRun.sh asterisk $2 $1 40