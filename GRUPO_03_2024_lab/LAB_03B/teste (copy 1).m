clear all
clc

A = [1 0; 0 -2];
B = [1 1]';
C = [1 1];

Polos = [-3 -3];

L = acker(A,C', Polos)

auto_valores = eig(A - L'*C)

I = eye(2)

Aa = [A 0*I; L'*C (A - L'*C)];
Ba = [B; B];
Ca = [C 0];