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
    
def Exemplo_2_ServossistemaTIPO_1(Polos=None):
    '''
    Exemplo 10.5 do livro de Ogata "Engenharia de Controle Moderno".

    Parametros do pêndulo invertido:
    Polos: Posições dos 5 polos desejados
    '''

    A = np.array([
        [0,1,0,0],
        [20.601, 0, 0, 0],
        [0,0,0,1],
        [-0.4905, 0, 0, 0]
        ])
    
    B = np.array([[0],[-1],[0],[0.5]])

    C = np.array([[0,0,1,0]])

    # Expandindo as matrizes para incluir o integrador
    Ahat = np.concatenate((A, np.zeros((4,1))), axis=1)
    temp = np.concatenate((-C, np.array([[0]])), axis=1)
    Ahat = np.concatenate((Ahat, temp), axis=0)

    Bhat = np.concatenate((B, np.array([[0]])), axis=0)

    del temp

    print("Matriz Ahat:\n", Ahat)
    print("Matriz Bhat:\n", Bhat)

    if Polos is None:
        Polos = [-1+2j*np.sqrt(3), -1-2j*np.sqrt(3),
                -1, -2, -3]
        
    K = ct.acker(Ahat, Bhat, Polos)
    print(K)

    KI = K[len(K)-1]
    K = np.copy(K[0:len(K)-1]).reshape(1,4)
    
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

    print(f'autovalores de Af = {np.linalg.eigvals(Af)}')

    del temp

    Bf = np.array([[0],[0],[0],[0],[1]])
    # Cf = np.concatenate((C, np.array([[0]])), axis=1)
    Cf = np.array([[0,0,0,0,1]])
    Df = np.array([[0]])

    print("Matriz Af:\n", Af)
    print("Matriz Bf:\n", Bf)
    print("Matriz Cf:\n", Cf)
    print("Matriz Df:\n", Df)

    # Resposta do sistema realimentado
    t, y = sg.step(sg.StateSpace(Af, Bf, Cf, Df))
    plt.plot(t, y)
    plt.title("Resposta ao Degrau do Servossistema Tipo 1 - Pêndulo Invertido")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Saída posição")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Exemplo_1_ServossistemaTIPO_1()
    Exemplo_2_ServossistemaTIPO_1()