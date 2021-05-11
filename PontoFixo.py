#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


def f(x):
    return x ** 2 + x - 6


def f2(x):
    return math.sqrt(6 - x)


def FixPoint(
    f,
    f2,
    x0,
    epsilon,
    iterMax=50,
    ):
    k = 1
    x1 = 0
    print 'k\t\t x0\t\t\t x1\t\t\t\t f(x0)'
    print ' -\t%e\t%e\t%e' % (x0, x1, f(x0))

    # # Inicie as iteracoes ( pode ser um for )

    for k in range(1, iterMax + 1):

        # # Em cada iteracao :
        # # Calcule x1 a partir de x0

        x1 = f2(x0)
        print '%d\t%e\t%e\t%e' % (k, x0, x1, f(x0))
        if abs(x0 - x1) < epsilon:
            return (False, x0)
        x0 = x1
        k = k + 1

    # # Se atingir o numero maximo de iteracoes mostra mensagem de erro e retorna
    # # a ultima raiz encontrada

    print ' ERRO ! numero maximo de iteracoes atingido .'
    return (True, x0)


x0 = 1.5
epsilon = 0.01
iterMax = 50
(houveErro, raiz) = FixPoint(f, f2, x0, epsilon, iterMax)
if houveErro:
    print 'O Metodo retornou um erro .'
if raiz is not None:
    print ' Raiz encontrada : %s' % raiz

			