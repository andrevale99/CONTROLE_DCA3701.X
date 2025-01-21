% *L1 = a11*L1 + b * Vp
% *L2 = a21*L1 + a22*L2
%
% dL1 = -a1 / A1 * sqrt(g / (2*L10)) * L1 + Km / A1 * Vp;
% dL2 = -a2 / A2 * sqrt(g / (2*L20)) * L2 + a1 / A2 * sqrt(g / (2*L10)) * L1;

% y = L2;

clear all
clc

g = 981; %aceleracao da gravidade (cm^2/s)
Km = 11.;

A1 = 15.5179; %area da secao transversal do tanque (cm^2)
A2 = A1;

a1 = 0.17813919765; %area do orifico (cm2^2)
a2 = a1;

L20 = 15; 
L10 = (a2^2 / a1^2) * L20;

A = [((-a1 / A1) * sqrt(g / (2*L10))) 0; 
    ((a1 / A2) * sqrt(g / (2*L10))) ((-a2 / A2) * sqrt(g / (2*L20)))];

B = [ Km/A1 0];
C = [0 1];

temp = zeros(1, length(B))';

A_aumentado = [0 C; temp A];
B_aumentado = [0; B'];

%Polos = [-0.1 ;-0.3 ; -0.5]; % Polos arbitrarios
%Polos = [-0.15 ;-0.3 ; -0.1]; % Polos arbitrarios
%Polos = [-0.3 ;-0.1 ; -0.1]; % Polos arbitrarios
Polos = [-0.3 ;-0.15 ; -0.15]; % Polos arbitrarios

K = -acker(A_aumentado, B_aumentado, Polos)

K1 = K(1,1)
K2 = K(2: length(K))

