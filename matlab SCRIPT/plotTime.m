clear;
close all;
filename = 'starTime.dat';
T = readtable(filename);
T= table2array(T);

plot(T(:,1),T(:,2))