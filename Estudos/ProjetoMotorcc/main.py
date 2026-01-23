import matplotlib.pyplot as plt
from scipy import signal as sg
import control as ct
import numpy as np
import sys
import os

Ra = 0
La = 0
KE = 0
KT = 0
J = 0
B = 0

filename = "data.txt"

def ArgvParser():
    '''
    Função para fazer o parsing dos argumentos passados via linha de comando.
    '''
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "-h" or sys.argv[i] == "--help":
                # Colocar mensagem de ajuda aqui
                print("Mensagem de ajuda")
                sys.exit(0)
            if sys.argv[i] == "-f" or sys.argv[i] == "--file":
                if i + 1 < len(sys.argv):
                    file_path = sys.argv[i + 1]
                    if os.path.isfile(file_path):
                        filename = file_path
                    else:
                        print(f"Erro: O arquivo '{file_path}' não existe.")
                        sys.exit(1)
                else:
                    print("Erro: Nenhum arquivo especificado após a opção '-f' ou '--file'.")
                    sys.exit(1)

# ============================================

def read_parameters(file_path):
    parameters = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            parameters[key] = float(value)
    return parameters

# ==============================================

def Seguidor_de_Referencia(A,B,C,D, Polos):
    # Aplicando o integrador ao sistema
    # Expandindo as matrizes para incluir o integrador
    Ahat = np.concatenate((A, np.zeros(B.shape)), axis=1)
    temp = np.concatenate((-C, np.array([[0]])), axis=1)
    Ahat = np.concatenate((Ahat, temp), axis=0)
    Bhat = np.concatenate((B, np.array([[0]])), axis=0)

    del temp

    K = ct.acker(Ahat, Bhat, Polos)
    print(f'Vetor de ganho K: {K}\n')
    KI = K[len(K)-1]
    K = np.copy(K[0:len(K)-1]).reshape(1,len(K)-1)

    print("Ganho de realimentação de estado K:\n", K, '\n')
    print("Ganho de realimentação de estado KI:\n", KI, '\n')

    # Aplicando no sistema realimentado
    A00 = A - (B * K)
    A01 = B * -KI
    A10 = -C
    A11 = np.array([[0]])

    Af = np.concatenate((A00, A01), axis=1)
    temp = np.concatenate((A10, A11), axis=1)
    Af = np.concatenate((Af, temp), axis=0)

    # print(f'Matriz A expandida:\n{Af}\n')

    print(f'Autovalores de A expandido: {np.linalg.eigvals(Af)}\n')

    del temp

    Bf = np.array([[0],[0],[1]])
    Cf = np.concatenate((C, np.array([[0]])), axis=1)
    Df = np.array([[0]])

    return Af, Bf, Cf, Df, K

# ==============================================

def Funcao_de_transferencia(A,B,C,D):
    num, den = sg.ss2tf(A, B, C, D)
    print("Função de Transferência G(s):\n")
    for s in range(len(num[0])):

        print(f"{num[0][s]}s^{len(num[0])-s-1}", end="")
        if s < len(num[0])-1:
            print(" + ", end="")
    print("\n---------")
    for s in range(len(den)):
        print(f"{den[s]}s^{len(den)-s-1}", end="")
        if s < len(den)-1:
            print(" + ", end="")
    print("\n")
    # print("Numerador:", num)
    # print("Denominador:", den)

    polos = np.roots(den)
    print("Polos de G(s):", polos, '\n')

    return num, den, polos

# ==============================================



if __name__ == "__main__":
    ArgvParser()
    params = read_parameters(filename)

    Ra = params.get('Ra', 1e-10)
    La = params.get('La', 1e-10)
    KE = params.get('KE', 1e-10)
    KT = params.get('KT', 1e-10)
    J = params.get('J', 1e-10)
    B = params.get('B', 1e-10)

    A = np.array([
    [-Ra/La, -KE/La],
    [KT/J, -B/J]
    ])

    B = np.array([[1/La],[0]])
    C = np.array([[0, 1]])
    D = np.array([[0]])

    print(f'Matriz A:\n{A}\n')
    print(f'Matriz B:\n{B}\n')
    print(f'Matriz C:\n{C}\n')
    print(f'Matriz D:\n{D}\n')
    print()

    sys = sg.StateSpace(A, B, C, D)
    time, yout = sg.step(sys)
    plt.plot(time, yout)
    plt.title("Resposta ao Degrau do Sistema Original")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()

    Funcao_de_transferencia(A,B,C,D)

    Af,Bf,_,Df,_ = Seguidor_de_Referencia(A,B,C,D, [-2+1j, -2-1j, -50])

    i = np.array([[1,0,0]])
    wm = np.array([[0,1,0]])
    e = np.array([[0,0,1]])

    # Resposta do sistema realimentado
    time, yout = sg.step(sg.StateSpace(Af, Bf, wm, Df))

    plt.plot(time, yout)
    plt.title("Resposta ao Degrau do Sistema com Seguidor de Referência")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()