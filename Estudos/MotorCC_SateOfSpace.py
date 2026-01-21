import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

Ra = 0.01
La = 0.25
KE = 0.01
KT = 0.01
J = 0.01
B = 0.001

A = np.array([
    [-Ra/La, -KE/La],
    [KT/J, -B/J]
])

B = np.array([[1/La],[0]])
C = np.array([[1, 0]])
D = np.array([[0]])

sys = sg.StateSpace(A, B, C, D)
t, y = sg.step(sys)

plt.plot(t, y)
plt.title("Resposta ao Degrau do Motor CC")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid()
plt.show()