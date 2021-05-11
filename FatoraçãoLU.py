#!/usr/bin/python
# -*- coding: utf-8 -*-


def substituicoes_sucessivas(A, b):

    # # n = a ordem da matriz A

    n = len(A)
    x = n * [0]
    x[0] = b[0] / A[0][0]
    for i in range(0, n):
        s = 0
        for j in range(0, i):
            s = s + A[i][j] * x[j]
            x[i] = (b[i] - s) / A[i][i]
    return x


def identidade(n):

    I = [[0 for y in range(n)] for x in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


def lu(A):
    n = len(A)

    # # Inicializa a matriz L com a matriz identidade

    L = identidade(n)
    for i in range(0, n):
        for j in range(i + 1, n):
            m = A[j][i] / A[i][i]
            L[j][i] = m
            for aux in range(n):
                A[j][aux] = A[j][aux] - m * A[i][aux]
    return (L, A)


def substituicoes_retroativas(A, b):

    # # n = a ordem da matriz A

    n = len(A)

    # # inicializa o vetor x com tamanho n e elementos iguais a 0

    y = n * [0]
    for i in range(n - 1, -1, -1):
        s = sum([A[i][j] * y[j] for j in range(i + 1, n)])
        y[i] = (b[i] - s) / A[i][i]
    return y


def resolve_lu(A, b):
    (L, U) = lu(A)
    y = substituicoes_sucessivas(L, b)
    x = substituicoes_retroativas(U, y)
    return x


import numpy as np
A = [[1, -3, 2], [-2, 8, -1], [4, -6, 5]]
b = [11, -15, 29]

v = np.copy(A)
x = resolve_lu(A, b)
print ('''
 Matriz Original : 
''', v)
(L, U) = lu(v)
print ('''
 Matriz L: 
''', L)
print ('''
 Matriz U: 
''', U)
print ('\n Vetor resposta : ', x)

			