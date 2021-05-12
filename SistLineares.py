def AproxMatriz(y1, q):#Matriz aproximada 
    n = len(y1)
    ax = 0
    i = 0
    while (i < n):
        ax += y1[i] * (q ** i) 
        i = i + 1
    return ax


def ordemMatriz(x, fx): 
    n = len(x)
    A = []
    # criar matriz i = 0
    while (i < n): 
        A.append([0] * n) 
        j = 0
        while (j < n): 
            j = j + 1
        i = i + 1
    # matriz criado i = 0
    while (i < n): 
        j = 0
        while (j < n):
            A[i][j] = x[i] ** j 
            j = j + 1
        i = i + 1
    # Ja tenho minha matriz A 
    return A


def substituicoes_retroativas(A, b):

    # Escreva o código aqui
    ## n é a ordem da matriz A 
    n = len(A)
    ## inicializa o vetor x com tamanho n e elementos iguais a 0
    x = n * [0]
    # escreva o seu código aqui # while n>=1:

    x[n - 1] = ((b[n - 1]) / (A[n - 1][n - 1]))

    i = (n - 1)

    while i >= 0:
        j = (i + 1)
        temp = b[i] 
        while j < n:
            temp -= (A[i][j] * x[j]) 
            j += 1

            x[i] = (temp / (A[i][i])) 
        i = i - 1

    return (x)

def gauss(A, b):

    ## n é a ordem da matriz A 
    n = len(A)
    k = 0
    while k < n:
        i = k+1 
        while i < n:
            m = A[i][k]/A[k][k]
            A[i][k] = 0
            j = k+1 
            while j < n:
                A[i][j] = A[i][j] - m*A[k][j] 
                j = j+1
            b[i] = b[i]- m*b[k] 
            i = i+1
        k = k+1

    ## Agora resolve o sistema triangular superior usando as substituições
    ## retroativas
    x = substituicoes_retroativas(A, b) 
    return x


q=-1 #Valor que quero achar 
x=[-2,0,2,3]
fx=[-18,4,10,22]
y = ordemMatriz(x,fx) 
y1= gauss(y,fx) 
print("Matriz: ",y) 
print("Resposta: ",y1)
resultado= AproxMatriz(y1,q) 
print("Aproximção sera: ",resultado)
 

