T_new = 1 / 10;         
n_new = 15393;           

%data = data{:,:}; 
czas_new = (0:T_new:(n_new-1)*T_new)';  
windowSize_new = 100;  
data_smoothed = movmean(data, windowSize_new); 
data_smoothed = data_smoothed - 25.362744000000010;


figure;


subplot(2, 1, 1);
plot(czas_new, data_smoothed);
xlabel('Czas [s]');
ylabel('Dane (wygładzone) Temperatura [C]');
title('Wykres wygładzony');
grid on;


subplot(2, 1, 2);
plot(czas_new, data);
xlabel('Czas [s]');
ylabel('Dane - Temperatura [C]');
title('Wykres oryginalny');
grid on;
