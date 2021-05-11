#!/usr/bin/python
# -*- coding: utf-8 -*-


def gauss_inversa(A):

    n = len(A)
    Inv = identidade(n)
    for i in range(n):
        m = A[i][i]
        for j in range(n):
            A[i][j] = A[i][j] / m
            Inv[i][j] = Inv[i][j] / m
        for k in range(n):
            if k != i:
                m = A[k][i]
                for j in range(n):
                    A[k][j] = A[k][j] - m * A[i][j]
                    Inv[k][j] = Inv[k][j] - m * Inv[i][j]
        i = i + 1
    return Inv


def identidade(n):
    I = [[0 for y in range(n)] for x in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


A = [[2, 1, 3], [0, -1, 1], [1, 0, 3]]
print ('\n Matriz Original : ', A)
print ('\n Inversa : ', gauss_inversa(A))

			