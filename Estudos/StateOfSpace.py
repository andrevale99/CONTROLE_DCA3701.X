import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

def ExampleRLC(R,L,C):
    '''
    Examplo de um sistema no espaco de estados
    de um circuito RLC em serie.

    Parâmetros:
    R : resistência (Ohms)
    L : indutância (mHenrys)
    C : capacitância (uFarads)
    '''

    A = np.array([[-R/L, -1/(L*C)],
                   [1, 0]])
    B = np.array([[1/L],
                   [0]])
    C = np.array([[0, 1]])
    D = np.array([[0]])

    num, den = sg.ss2tf(A, B, C, D)
    print("Função de Transferência:")
    print("Numerador:", num)
    print("Denominador:", den)

    polos = np.roots(den)
    print("Polos de G(s):", polos)

    sys = sg.StateSpace(A, B, C, D)
    t, y = sg.step(sys)

    plt.plot(t, y)
    plt.title("Resposta ao Degrau do Circuito RLC")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()

def ExampleMOTORCC(Params):
    '''
    Exemplo de um sistema no espaço de estados
    de um motor de corrente contínua.

    Parâmetros do motor:

    Ra : resistência do armadura (Ohms)
    La : indutância do armadura (Henrys)
    J  : momento de inércia (kg.m^2)
    b  : coeficiente de atrito viscoso (N.m.s)
    Kt : constante de torque (N.m/A)
    Ke : constante de força contra-eletromotriz (V.s/rad)

    Nota: Params é uma lista ou array com os parâmetros na ordem acima.
    '''

    Ra = Params[0]      # resistência do armadura (Ohms)
    La = Params[1]      # indutância do armadura (Henrys)
    J = Params[2]       # momento de inércia (kg.m^2)
    b = Params[3]       # coeficiente de atrito viscoso (N.m.s)
    Kt = Params[4]      # constante de torque (N.m/A)
    Ke = Params[5]      # constante de força contra-eletromotriz (V.s/rad)

    A = np.array([[-Ra/La, -Ke/La],
                   [Kt/J, -b/J]])
    B = np.array([[1/La],
                   [0]])
    C = np.array([[1, 0]])
    D = np.array([[0]])

    print("A:\n", A)
    print("B:\n", B)
    print("C:\n", C)
    print("D:\n", D)
    print()

    num, den = sg.ss2tf(A, B, C, D)
    print("Função de Transferência do Motor CC:")
    print("Numerador:", num)
    print("Denominador:", den)

    polos = np.roots(den)
    print("Polos de G(s):", polos)

    sys = sg.StateSpace(A, B, C, D)
    t, y = sg.step(sys)

    plt.plot(t, y)
    plt.title("Resposta ao Degrau do Motor CC")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade Angular (rad/s)")
    plt.grid()
    plt.show() 

if __name__ == "__main__":
    # ExampleRLC(100, 1e-1, 1e-6)

    # Ra, La, J, b, Kt, Ke
    Params = [1, 0.15, 0.01, 0.1, 1, 1]
    ExampleMOTORCC(Params)
