import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg
import control as ct

def Exemplo_1_ServossistemaTIPO_1():
    '''
    Exemplo de projeto de um servossistema do tipo 1
    com um integrador. Exemplo 10.4 do livro de Ogata
    "Engenharia de Controle Moderno".

    Y(s) / U(s) = 1 / (s(s+2)(s+3))
    '''

    A = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [0, -2, -3]
    ])

    B = np.array([[0],[0],[1]])
    C = np.array([[1, 0, 0]])
    D = np.array([[0]])

    polos = [-2+2j*np.sqrt(3), -2-2j*np.sqrt(3), -10]

    k = ct.acker(A, B, polos)

    print("Ganho de realimentação de estado K:", k)

    # Sistema com realimentação de estado
    # A - Bk

    Aa = A - B @ k.reshape(1,3)
    print("Matriz A do sistema realimentado:\n", Aa)

    Ba = B * k[0]  # Entrada de referência
    print("Matriz B do sistema realimentado:\n", Ba)

    Ca = C
    print("Matriz C do sistema realimentado:\n", Ca)

    Da = D
    print("Matriz D do sistema realimentado:\n", Da)
    print()

    t, y = sg.step(sg.StateSpace(Aa, Ba, Ca, Da))
    plt.plot(t, y)
    plt.title("Resposta ao Degrau do Servossistema Tipo 1")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    Exemplo_1_ServossistemaTIPO_1()