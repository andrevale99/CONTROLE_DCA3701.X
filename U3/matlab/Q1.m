clear all
clc

A = [0 1 0; 0 0 1; -1 -5 -6];
B = [0 1 1]';
C = [1 0 0];

Pc = [-1+4j -1-4j -10];

%qc = (A*A*A) + 12*A*A + 37*A + 170*eye(3,3);
%U = [B A*B A*A*B]
%U_inv = inv(U)

%K = -[0 0 1] * U_inv * qc

K = -acker(A,B,Pc)

Aa = [A+B*K];
Ba = [B];
Ca = [1 0 0];


t = 0:0.1:10;
u = 0*t;
x0 = [1 0 0]';

sys = ss(Aa, Ba, Ca, 0);
[Y X] = lsim(sys, u, t, x0);

title('Saída com Realimentação')
plot(t, Y)