#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def Sassenfeld(A):
    n = len(A)
    i = 0
    x = n * [0]

    # x = 0,0,0

    y = n * [1]

    # y= 1,1,1

    soma = 0
    while i < n:
        j = 0
        soma = 0
        while j < n:
            if i != j:
                x[j] = A[i][j] * y[j]
                soma = x[j] + soma
            j = j + 1

        # return soma

        x[i] = soma / A[i][i]

        # return x

        y[i] = x[i]

        # y = np. copy (x)

        i = i + 1
    maior = 0
    i = 0
    while i < n:
        if y[i] > maior:
            maior = y[i]
        i = i + 1
    print '\n'
    if maior < 1:
        print 'O metodo de Gauss - Seidel convergira '
        print (maior, ' < 1')
    else:
        print 'O metodo de Gauss - Seidel NAO convergira '


def norma(v, x):
    n = len(v)
    d = n * [0]
    maior = 0
    maiorNEW = 0
    i = 0
    j = 0
    while j < n:
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


def seidel(
    A,
    b,
    epsilon,
    iterMax=15,
    ):
    n = len(A)
    x = n * [0]
    v = n * [0]
    tol = 1
    d = 0
    i = 0
    while i < n:
        v[i] = 0
        i = i + 1

    # V sera o meu X inicial
    # [0, 0, 0]

    while tol < iterMax:
        i = 0
        while i < n:
            j = 0
            x[i] = b[i]
            while j < n:
                if i != j:
                    x[i] -= A[i][j] * x[j]
                j = j + 1
            x[i] = x[i] / A[i][i]
            i = i + 1
        print (' Vetor X', tol - 1, ' :', v)
        print (' Vetor X', tol, ' :', x)
        d = norma(v, x)
        print (' Norma : ', d)
        print '\n'
        i = 0
        while i < n:
            v[i] = x[i]
            i = i + 1
        if d < epsilon:
            print ('O metodo converge em ', tol, ' iteracoes ')
            return x
        tol = tol + 1
    print ' Numero maximo de iteracao atingida '


A = [[5, 1, 1], [3, 4, 1], [3, 3, 6]]
b = [5, 6, 0]
epsilon = 0.05
iterMax = 15
res = Sassenfeld(A)
print res
print '\n'
x = seidel(A, b, epsilon, iterMax)
print x

			