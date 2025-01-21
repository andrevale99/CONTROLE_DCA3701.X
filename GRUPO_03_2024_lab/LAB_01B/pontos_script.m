clear
clc

exp_5 = [0.7050 0.6982 0.7611 0.7665 0.7256];
exp_10 = [1.5600	1.5137	1.5540	1.5320	1.5260];
exp_15 = [2.4440	2.3740	2.3540	2.3430	2.3330];
exp_20 = [3.1450	3.1550	3.1620	3.1620	3.1540];
exp_25 = [3.9750	3.9580	3.9430	3.9340	3.9420];


mean_exp_5 = mean(exp_5);
mean_exp_10 = mean(exp_10);
mean_exp_15 = mean(exp_15);
mean_exp_20 = mean(exp_20);
mean_exp_25 = mean(exp_25);

x = [5 10 15 20 25];

y = mean_exp_15 - mean_exp_10
inclinacao = y / 5
nome = 1 / inclinacao

scatter(mean_exp_5, x(1))

xlabel('Tensao (V)')
ylabel('Altura (cm)')
xlim([0 4.5])
ylim([0 28])
grid()

hold on
scatter(mean_exp_10, x(2))
hold on
scatter(mean_exp_15, x(3))
hold on
scatter(mean_exp_20, x(4))
hold on
scatter(mean_exp_25, x(5))
hold on
