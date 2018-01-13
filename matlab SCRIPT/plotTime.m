clear;
close all;

%%%Carico le varie tabelle
filename = 'starTime.dat';
T = readtable(filename);
global star
star= table2array(T);

filename = 'fractalSon2_Time.dat';
T = readtable(filename);
global fractal2
fractal2= table2array(T);

filename = 'fractalSon25_Time.dat';
T = readtable(filename);
global fractal25
fractal25= table2array(T);

filename = 'fractalSon100_Time.dat';
T = readtable(filename);
global fractal100
fractal100= table2array(T);

filename = 'fractalSon250_Time.dat';
T = readtable(filename);
global fractal250
fractal250= table2array(T);

filename = 'fractalSon500_Time.dat';
T = readtable(filename);
global fractal500
fractal500= table2array(T);

filename = 'linearTime.dat';
T = readtable(filename);
global linear
linear= table2array(T);

filename = 'rand2Son100_Time.dat';
T = readtable(filename);
global sfilacciato
sfilacciato= table2array(T);

filename = 'randTime.dat';
T = readtable(filename);
global random
random= table2array(T);


f1 = figure;
f2 = figure;

figure(f1);
subplot(1,2,1);
hold on
% creo il grafico concatenando le varie tabelle
plotAll();
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Tutte le funzioni')


subplot(1,2,2);
hold on
% creo il grafico concatenando le varie tabelle
set(gca, 'YScale', 'log')
plotAll();
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Confronto Logaritmico')

hold off

figure(f2); 
%scatter((1:20),rand(1,20));
subplot(1,2,1);
hold on
% creo il grafico concatenando le varie tabelle
plot(star(:,1),star(:,2),'g','DisplayName','Stella')
plot(fractal2(:,1),fractal2(:,2),'r','DisplayName','D-heap 2')
plot(sfilacciato(:,1),sfilacciato(:,2),'c','DisplayName','FiloSfilacciato')
plot(random(:,1),random(:,2),'k','DisplayName','Casuale')
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Fig1')



function [] = plotAll( )
global linear
global star
global random
global sfilacciato
global fractal2
global fractal25
global fractal100
global fractal250
global fractal500

plot(linear(:,1),linear(:,2),'b','DisplayName','Lineare')
plot(star(:,1),star(:,2),'g','DisplayName','Stella')
plot(random(:,1),random(:,2),'k','DisplayName','Casuale')
plot(sfilacciato(:,1),sfilacciato(:,2),'c','DisplayName','FiloSfilacciato')
plot(fractal2(:,1),fractal2(:,2),'r','DisplayName','D-heap 2')
plot(fractal25(:,1),fractal25(:,2),'m','DisplayName','D-heap 25')
plot(fractal100(:,1),fractal100(:,2),'Color',[1,0.5,0],'DisplayName','D-heap 100')
plot(fractal250(:,1),fractal250(:,2),'Color',[1,0,0.5],'DisplayName','D-heap 250')
plot(fractal500(:,1),fractal500(:,2),'Color',[0,0.6,0.5],'DisplayName','D-heap 500')

end

