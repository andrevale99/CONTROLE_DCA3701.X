A1_cm = 4.445;
a1_cm = 0.47625;

% Erro de calibracao do sensor
h_cm = 26;

tensao = [1:0.3:4];
tempo_1_1V_s = [36.81 36.62 34.64 34.5 35.06];
tempo_2_13V_s = [27.45 25.89 26.29 26.25 27.17];
tempo_3_16V_s = [22.94 21.49 20.93 21.23 20.87];
tempo_4_19V_s = [18.8 17.25 17.59 17.45 17.29];
tempo_5_22V_s = [16.31 14.96 14.94 14.92 14.98];
tempo_6_25V_s = [14.36 13.27 13.29 13.29 13.38];
tempo_7_28V_s = [13.09 12.02 12.02 11.93 12.01];
tempo_8_31V_s = [11.89 10.9 10.93 10.91 10.88];
tempo_9_34V_s = [10.95 10.05 10.08 10.05 10.15];
tempo_10_37V_s = [10.15 9.344 9.362 9.43 9.306];
tempo_11_4V_s = [9.368 8.752 8.724 8.756 8.726];

medias_dos_tempos = [mean(tempo_1_1V_s) mean(tempo_2_13V_s) mean(tempo_3_16V_s)
       mean(tempo_4_19V_s) mean(tempo_5_22V_s) mean(tempo_6_25V_s)
       mean(tempo_7_28V_s) mean(tempo_8_31V_s) mean(tempo_9_34V_s)
       mean(tempo_10_37V_s) mean(tempo_11_4V_s)]