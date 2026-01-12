import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

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
plt.title("Resposta ao Degrau do Circuito RLC")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid()
plt.show()
