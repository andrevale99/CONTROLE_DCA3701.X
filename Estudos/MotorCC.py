import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg
import control as ct

"""
Exemplo de um sistema no espaço de estados
de um motor de corrente contínua.
"""

Ra = 1.0    # Resistência do armadura (Ohms)
La = 0.5    # Indutância do armadura (Henrys)
ke = 0.01   # Constante de força contra-eletromotriz (V/rad/s)
kt = 0.01   # Constante de torque (Nm/A)
K = ke
J = 0.01    # Momento de inércia do rotor (kg.m^2)
B = 0.1     # Coeficiente de atrito viscoso (N.m)

V = 120    # Tensão aplicada (Volts)

den = [1, (B/J + Ra/La), (Ra*B + K**2)/(J*La)]
num = [K/(J*La)]

print("Função de Transferência:")
print("Numerador:", num)
print("Denominador:", den)
print()

A, B, C, D = sg.tf2ss(num, den)

print("A:\n",A)
print("B:\n",B)
print("C:\n",C)
print("D:\n",D)

# Matriz de Controlabilidade
U = np.concatenate((B, A @ B), axis=1)
rank_U = np.linalg.matrix_rank(U)
print("\nMatriz de Controlabilidade U:\n", U)
print("Posto da Matriz de Controlabilidade:", rank_U)

sys = sg.StateSpace(A, B, C, D)
t, y = sg.step(sys)

plt.plot(t, y)
plt.title("Resposta ao Degrau do motor CC")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid()
plt.show()

# Expandindo as matrizes para incluir o integrador
Ahat = np.concatenate((A, np.zeros((2,1))), axis=1)
temp = np.concatenate((-C, np.array([[0]])), axis=1)
Ahat = np.concatenate((Ahat, temp), axis=0)
Bhat = np.concatenate((B, np.array([[0]])), axis=0)

del temp

print("Matriz Ahat:\n", Ahat)
print("Matriz Bhat:\n", Bhat)

Polos = [-2+1j*np.sqrt(3), -2-1j*np.sqrt(3), -10]
    
K = ct.acker(Ahat, Bhat, Polos)
print(K)
KI = K[len(K)-1]
K = np.copy(K[0:len(K)-1]).reshape(1,len(K)-1)

print("Ganho de realimentação de estado K:\n", K)
print("Ganho de realimentação de estado KI:\n", KI)

# Aplicando no sistema realimentado
A00 = A - (B * K)
A01 = B * -KI
A10 = -C
A11 = np.array([[0]])
    
Af = np.concatenate((A00, A01), axis=1)
temp = np.concatenate((A10, A11), axis=1)
Af = np.concatenate((Af, temp), axis=0)

del temp

Bf = np.array([[0],[0],[1]])
Cf = np.concatenate((C, np.array([[0]])), axis=1)
Df = np.array([[0]])

print("Matriz Af:\n", Af)
print("Matriz Bf:\n", Bf)
print("Matriz Cf:\n", Cf)
print("Matriz Df:\n", Df)

# Resposta do sistema realimentado
t, y = sg.step(sg.StateSpace(Af, Bf, Cf, Df))
plt.plot(t, y)
plt.title("Resposta ao Degrau do Servossistema Tipo 1 - motor CC")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid()
plt.show()

