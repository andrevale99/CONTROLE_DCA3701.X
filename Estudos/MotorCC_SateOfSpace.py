import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg
import control as ct


Ra = 0.01
La = 0.25
KE = 0.01
KT = 0.01
J = 0.01
B = 0.001

# Polos que serao realocados
# Polos = [-2+1j*np.sqrt(3), -2-1j*np.sqrt(3), -10]
Polos = [-2, -2, -1]

A = np.array([
    [-Ra/La, -KE/La],
    [KT/J, -B/J]
])

B = np.array([[1/La],[0]])
C = np.array([[0, 1]])
D = np.array([[0]])

sys = sg.StateSpace(A, B, C, D)
t1, y1 = sg.step(sys)

# Aplicando o integrador ao sistema
# Expandindo as matrizes para incluir o integrador
Ahat = np.concatenate((A, np.zeros(B.shape)), axis=1)
temp = np.concatenate((-C, np.array([[0]])), axis=1)
Ahat = np.concatenate((Ahat, temp), axis=0)
Bhat = np.concatenate((B, np.array([[0]])), axis=0)

del temp
    
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

print(np.linalg.eigvals(Af))

del temp

Bf = np.array([[0],[0],[1]])
Cf = np.concatenate((C, np.array([[0]])), axis=1)
Df = np.array([[0]])

# Resposta do sistema realimentado
t2, y2 = sg.step(sg.StateSpace(Af, Bf, Cf, Df))

fig = plt.figure()
fig1 = fig.add_subplot(2, 1, 1)
fig1.plot(t1, y1)
fig1.set_title("Resposta ao Degrau do Motor CC")
fig1.set_xlabel("Tempo (s)")
fig1.set_ylabel("Saída")
fig1.grid()

fig2 = fig.add_subplot(2, 1, 2)
fig2.plot(t2, y2)
fig2.set_title("Resposta ao Degrau do Servossistema Tipo 1 - motor CC")
fig2.set_xlabel("Tempo (s)")
fig2.set_ylabel("Saída")
fig2.grid()

fig.tight_layout()

plt.show()