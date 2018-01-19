# Progetto-2
Sviluppato da:
1) Filippo Badalamenti (Team Leader)
2) Marta Caggiano
3) Emanuele Alfano

#Primo avvio di demoMain.py

Al primo avvio del progetto sarà sufficente avviare con python3.6 il file senza alcun parametro e verra printata sul command la help della funzione con la sintassi da applicare per le singole forme.

#Sintassi script Bash
Per runnare il progamma bash che esegue e salva in automatico i dati:

1) ./runAndData.sh >forma< >output del medio< >nElem> >OutFileDir> >son< >outDircProfile< 
2) ./serialRun.sh >forma<  >nIteration(50*n)<  >OutFileDir<  >son< 
3) ./esecuzioniForme.sh >OutFileDir< >nIteration(50*n)<

#Regole Di sintassi
Regole di sintassi:
1) Le aggiunte nel codice dei prof devono avere vicino al def:
"#ACB" ovvero Alfano Caggiano Badalamenti

#Lista modifiche a codice pregresso
Lista Funzioni modificate o aggiunte:
1) graph/Graph_AdjacencyList aggiunto "getAdjList"
2) graph/Graph_AdjacencyList modificato pesantemente "getAdj"
3) graph/Graph_AdjacencyList fatto l'override di del per eliminare il grafo, ma commentato perchè non sembra ridurre la memoria ma allunga i tempi
4) list/LinkedList.py fatto l'override di del per eliminare il grafo
5) UninonFind_QuickFind overridie di __str__ per printare l'union
6) UninonFind_QuickUnion overridie di __str__ per printare l'union

#Matlab Script
Lo script matlab riceve una tabella csv su file .dat, e li converte nei 3 grafici presenti nella relazione.
la versione di matlab è la 2017.a eseguita su linux (Kubuntu)