clear;
close all;

%%%Carico le varie tabelle
filename = 'starTime.dat';
T = readtable(filename);
star= table2array(T);


filename = 'fractalSon2_Time.dat';
T = readtable(filename);
fractal= table2array(T);


filename = 'linearTime.dat';
T = readtable(filename);
linear= table2array(T);

filename = 'rand2Son100_Time.dat';
T = readtable(filename);
sfilacciato= table2array(T);

filename = 'randTime.dat';
T = readtable(filename);
random= table2array(T);



subplot(1,2,1);
% creo il grafico concatenando le varie tabelle
plot(star(:,1),star(:,2),'g',fractal(:,1),fractal(:,2),'r',linear(:,1),linear(:,2),'b',sfilacciato(:,1),sfilacciato(:,2),'c',random(:,1),random(:,2),'k')
legend('Stella','Frattale','Lineare','Sfilacciato','Random')
%Predispongo il plot dei dato
hold on
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Tutte le funzioni')


subplot(1,2,2);
% creo il grafico concatenando le varie tabelle
semilogy(star(:,1),star(:,2),'g',fractal(:,1),fractal(:,2),'r',linear(:,1),linear(:,2),'b',sfilacciato(:,1),sfilacciato(:,2),'c',random(:,1),random(:,2),'k')
legend('Stella','Frattale','Lineare','Sfilacciato','Random')
%Predispongo il plot dei dato
hold on
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Confronto Logaritmico delle stesse')