import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg
import control as ct

"""
Exemplo 10.7 - Projeto de um Observador de Estados
do livro do OGATA.
"""

A = np.array([[0, 1],
                [20.6, 0]])

B = np.array([[0],[1]])
C = np.array([[1, 0]])
D = np.array([[0]])

Polos_Sistema = [-1.8+2.4j, -1.8-2.4j]
Polos_Observador = [-8, -8]


K = ct.acker(A, B, Polos_Sistema).reshape(1,2)
print("Ganho de realimentação de estado K:\n", K)

L = ct.acker(A.T, C.T, Polos_Observador).reshape(2,1)
print("Ganho de observador L:\n", L)

A00 = A - (B @ K)
A01 = B @ K
A10 = np.zeros((2,2))
A11 = A - (L @ C)

Aa = np.concatenate((A00, A01), axis=1)
temp = np.concatenate((A10, A11), axis=1)
Aa = np.concatenate((Aa, temp), axis=0)

print("Matriz Aa:\n", Aa)

Ba = np.array([[0],[0],[0],[1]])
Ca = np.array([[1,0,0,0]])
Da = np.zeros((1,1))

# Resposta do sistema realimentado
t, y = sg.step(sg.StateSpace(Aa, Ba, Ca, Da))
plt.plot(t, y)
plt.title("Resposta ao Degrau do Sistema com Observador")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid()
plt.show()