clear;
close all;
%Predispongo il plot dei dati
hold on
grid on
xlabel("Numero di elementi")
ylabel("Time to find MED")
legend('Location','northwest')


%%%Carico le varie tabelle
filename = 'starTime.dat';
T = readtable(filename);
star= table2array(T);


filename = 'fractalTime.dat';
T = readtable(filename);
fractal= table2array(T);


filename = 'linearTime.dat';
T = readtable(filename);
linear= table2array(T);


% creo il grafico concatenando le varie tabelle
plot(star(:,1),star(:,2),'g',fractal(:,1),fractal(:,2),'r',linear(:,1),linear(:,2))
legend('stella','Frattale','lineare')
