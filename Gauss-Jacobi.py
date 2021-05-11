#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def Linha(A):

    # Criterio das linhas

    n = len(A)
    i = 0
    soma = 0
    while i < n:
        j = 0
        soma = 0
        while j < n:
            if i != j:
                soma = A[i][j] + soma
            j = j + 1
        if A[i][i] > soma:
            print (
                ' Linha ',
                i + 1,
                ' obedecido , pois ',
                A[i][i],
                ' e maior que ',
                soma,
                )
        else:
            print (
                ' Linha ',
                i + 1,
                ' NAO foi obedecido , pois ',
                A[i][i],
                ' NAO e maior que ',
                soma,
                )
        i = i + 1
    print '\n'


def norma(v, x):
    n = len(v)
    d = n * [0]
    maior = 0
    maiorNEW = 0
    i = 0
    j = 0
    while j < n:

        # sempre calculando o valor absoluto

        if abs(x[j]) > maiorNEW:
            maiorNEW = abs(x[j])
        j = j + 1
    while i < n:
        d[i] = abs(x[i]) - abs(v[i])
        if abs(d[i]) > maior:
            maior = d[i]
        i = i + 1
    d = maior / maiorNEW
    return d


def jacobi(
    A,
    b,
    epsilon,
    iterMax=11,
    ):

    n = len(A)
    x = n * [0]
    v = n * [0]
    tol = 0
    d = 0
    i = 0
    while i < n:
        v[i] = b[i] / A[i][i]
        i = i + 1

    # V sera o meu X inicial
    # [0.7 , -1.6, 0.6]

    while tol < iterMax:
        tol = tol + 1
        i = 0
        while i < n:
            j = 0
            x[i] = b[i]
            while j < n:
                if i != j:
                    x[i] -= A[i][j] * v[j]
                j = j + 1
            x[i] = x[i] / A[i][i]
            i = i + 1
        d = norma(v, x)

        # Printar os valores de X

        print (' Vetor X', tol - 1, ' :', v)
        print (' Vetor X', tol, ' :', x)
        print (' Norma : ', d)
        print '\n'
        i = 0

        # copiar o valor de X para o meu vetor V

        v = np.copy(x)
        if d < epsilon:
            print ('O metodo converge em ', tol, ' iteracoes ')
            return x
        i = 0

        # Reinicio meu Vetor X, ou seja , o vetor sera de zeros

        while i < n:
            x[i] = 0
            i = i + 1
    print ' Numero maximo de iteracao atingida '


A = [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
b = [7, -8, 6]
epsilon = 0.05
iterMax = 11
print '\n'
print Linha(A)
x = jacobi(A, b, epsilon, iterMax)
print x

			