clear all
clc

A = [0 1 0; 0 0 1; -6 -11 -6];
B = [0 0 1]';
C = [1 0 0];

Pc = [-1+1j -1-1j -5]
Po = [-6 -6 -6]

K = -acker(A, B, Pc)

L = acker(A', C', Po)'

Aa = [A B*K ; L*C (A - L*C + B*K)];
Ba = [B;B];
Ca = [C 0 0 0];

t = 0:0.1:10;
u = 0*t;
x0 = [1 0 0 0 0 0]';

sys = ss(Aa, Ba, Ca, 0);
[Y X] = lsim(sys, u, t, x0)

title('Saída com Realimentação + Observador')
plot(t, Y)
