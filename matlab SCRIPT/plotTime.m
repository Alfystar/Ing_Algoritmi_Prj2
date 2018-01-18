clear;
close all;

%%%Carico le varie tabelle
%%%%asterisko
filename = 'asteriscoSon5_Time.dat';
T = readtable(filename);
global asterisco5
asterisco5= table2array(T);

filename = 'asteriscoSon25_Time.dat';
T = readtable(filename);
global asterisco25
asterisco25= table2array(T);

% filename = 'asteriscoSon40_Time.dat';
% T = readtable(filename);
% global asterisco40
% asterisco40= table2array(T);

%%%%frattali
filename = 'fractalSon2_Time.dat';
T = readtable(filename);
global fractal2
fractal2= table2array(T);

filename = 'fractalSon25_Time.dat';
T = readtable(filename);
global fractal25
fractal25= table2array(T);

% filename = 'fractalSon100_Time.dat';
% T = readtable(filename);
% global fractal100
% fractal100= table2array(T);

filename = 'linearTime.dat';
T = readtable(filename);
global linear
linear= table2array(T);

filename = 'randTime.dat';
T = readtable(filename);
global random
random= table2array(T);

% filename = 'sfilacciatoRandSon5_Time.dat';
% T = readtable(filename);
% global sfilacciatoRand
% sfilacciatoRand= table2array(T);

filename = 'sfilacciatoSon2_Time.dat';
T = readtable(filename);
global sfilacciato
sfilacciato= table2array(T);

filename = 'starTime.dat';
T = readtable(filename);
global star
star= table2array(T);


x=star(1,2)/10 %tempo teorico per 1 elemento
global logTime
logTime=(star(:,1)).*log10((star(:,1)))*x


Normale = figure;

figure(Normale);
%subplot(1,2,1);
hold on
% creo il grafico concatenando le varie tabelle
plotAll();
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Confronto Lineare')
hold off


 Doppio_logaritmico = figure;
 figure(Doppio_logaritmico); 
%subplot(1,2,2);
hold on
% creo il grafico concatenando le varie tabelle
set(gca, 'YScale', 'log')
set(gca, 'XScale', 'log')
plotAll();
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Pendenza Asisitotica')

 X_log = figure;
 figure(X_log); 
%subplot(1,2,2);
hold on
% creo il grafico concatenando le varie tabelle
set(gca, 'YScale', 'log')
%set(gca, 'XScale', 'log')
plotAll();
legend('Show')
%Predispongo il plot dei dato
grid on
xlabel("N° elem")
ylabel("Time to find MED")
legend('Location','northwest')
title('Crescita Logaritmica')



% f2 = figure;
% figure(f2); 
% %scatter((1:20),rand(1,20));
% subplot(1,2,1);
% hold on
% % creo il grafico concatenando le varie tabelle
% plot(star(:,1),star(:,2),'g','DisplayName','Stella')
% plot(fractal2(:,1),fractal2(:,2),'r','DisplayName','D-heap 2')
% plot(sfilacciato(:,1),sfilacciato(:,2),'c','DisplayName','FiloSfilacciato')
% plot(random(:,1),random(:,2),'k','DisplayName','Casuale')
% legend('Show')
% %Predispongo il plot dei dato
% grid on
% xlabel("N° elem")
% ylabel("Time to find MED")
% legend('Location','northwest')
% title('Fig1')



function [] = plotAll( )
global asterisco5
global asterisco25
global fractal2
global fractal25
% global fractal100
global linear
global random
% global sfilacciatoRand
global sfilacciato
global star

global logTime


width=2

plot(linear(:,1),linear(:,2),'b','LineWidth',width,'DisplayName','Lineare')
plot(star(:,1),star(:,2),'Color',hex2rgb('#00E100'),'LineWidth',width,'DisplayName','Stella')                                  %giada
plot(random(:,1),random(:,2),'Color',hex2rgb('#FF0080'),'LineWidth',width,'DisplayName','Casuale')           %arancio bruciato

plot(star(:,1),logTime(:,1),'Color',hex2rgb('#00C0FF'),'LineWidth',width,'DisplayName','LogTime teorico')           


plot(sfilacciato(:,1),sfilacciato(:,2),'Color',hex2rgb('#ABCDEF'),'LineWidth',width,'DisplayName','Sfilacciato-2')  %azzurro fiordaliso

% plot(sfilacciatoRand(:,1),sfilacciatoRand(:,2),'c','DisplayName','FiloSfilacciato')

plot(fractal2(:,1),fractal2(:,2),'Color',hex2rgb('#008250'),'LineWidth',width,'DisplayName','D-heap 2')                 %nocciola
plot(fractal25(:,1),fractal25(:,2),'-.','Color',hex2rgb('#008250'),'LineWidth',width,'DisplayName','D-heap 25')

% plot(fractal100(:,1),fractal100(:,2),'Color',[1,0.5,0],'DisplayName','D-heap 100')

plot(asterisco5(:,1),asterisco5(:,2),'Color',hex2rgb('#FFA500'),'LineWidth',width,'DisplayName','Asterisco 5')    %arancione
plot(asterisco25(:,1),asterisco25(:,2),'-.','Color',hex2rgb('#FFA500'),'LineWidth',width,'DisplayName','Asterisco 25')
end


function [ rgb ] = hex2rgb(hex,range)
% hex2rgb converts hex color values to rgb arrays on the range 0 to 1. 
% 
% 
% * * * * * * * * * * * * * * * * * * * * 
% SYNTAX:
% rgb = hex2rgb(hex) returns rgb color values in an n x 3 array. Values are
%                    scaled from 0 to 1 by default. 
%                    
% rgb = hex2rgb(hex,256) returns RGB values scaled from 0 to 255. 
% 
% 
% * * * * * * * * * * * * * * * * * * * * 
% EXAMPLES: 
% 
% myrgbvalue = hex2rgb('#334D66')
%    = 0.2000    0.3020    0.4000
% 
% 
% myrgbvalue = hex2rgb('334D66')  % <-the # sign is optional 
%    = 0.2000    0.3020    0.4000
% 
%
% myRGBvalue = hex2rgb('#334D66',256)
%    = 51    77   102
% 
% 
% myhexvalues = ['#334D66';'#8099B3';'#CC9933';'#3333E6'];
% myrgbvalues = hex2rgb(myhexvalues)
%    =   0.2000    0.3020    0.4000
%        0.5020    0.6000    0.7020
%        0.8000    0.6000    0.2000
%        0.2000    0.2000    0.9020
% 
% 
% myhexvalues = ['#334D66';'#8099B3';'#CC9933';'#3333E6'];
% myRGBvalues = hex2rgb(myhexvalues,256)
%    =   51    77   102
%       128   153   179
%       204   153    51
%        51    51   230
% 
% HexValsAsACharacterArray = {'#334D66';'#8099B3';'#CC9933';'#3333E6'}; 
% rgbvals = hex2rgb(HexValsAsACharacterArray)
% 
% * * * * * * * * * * * * * * * * * * * * 
% Chad A. Greene, April 2014
%
% Updated August 2014: Functionality remains exactly the same, but it's a
% little more efficient and more robust. Thanks to Stephen Cobeldick for
% the improvement tips. In this update, the documentation now shows that
% the range may be set to 256. This is more intuitive than the previous
% style, which scaled values from 0 to 255 with range set to 255.  Now you
% can enter 256 or 255 for the range, and the answer will be the same--rgb
% values scaled from 0 to 255. Function now also accepts character arrays
% as input. 
% 
% * * * * * * * * * * * * * * * * * * * * 
% See also rgb2hex, dec2hex, hex2num, and ColorSpec. 
% 

%% Input checks:

assert(nargin>0&nargin<3,'hex2rgb function must have one or two inputs.') 

if nargin==2
    assert(isscalar(range)==1,'Range must be a scalar, either "1" to scale from 0 to 1 or "256" to scale from 0 to 255.')
end

%% Tweak inputs if necessary: 

if iscell(hex)
    assert(isvector(hex)==1,'Unexpected dimensions of input hex values.')
    
    % In case cell array elements are separated by a comma instead of a
    % semicolon, reshape hex:
    if isrow(hex)
        hex = hex'; 
    end
    
    % If input is cell, convert to matrix: 
    hex = cell2mat(hex);
end

if strcmpi(hex(1,1),'#')
    hex(:,1) = [];
end

if nargin == 1
    range = 1; 
end

%% Convert from hex to rgb: 

switch range
    case 1
        rgb = reshape(sscanf(hex.','%2x'),3,[]).'/255;

    case {255,256}
        rgb = reshape(sscanf(hex.','%2x'),3,[]).';
    
    otherwise
        error('Range must be either "1" to scale from 0 to 1 or "256" to scale from 0 to 255.')
end

end

