#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import exp, cos, sin


def f(x):
    return x ** 4 - 6 * x ** 3 + 10 * x ** 2 - 6 * x + 9


def flin(x):
    return 4 * x ** 3 - 18 * x ** 2 + 20 * x - 6


def newton(
    f,
    flin,
    x0,
    epsilon,
    iterMax=50,
    ):

    # # Teste se x0 ja e logo a raiz

    print 'k\t\t x0\t\t x1\t\t\t\t f(x1)\t\t\t flin (x0)'
    k = 1
    if x0 < epsilon:
        return (False, x0)
    ab = f(x0)

    # # Inicie as iteracoes ( pode ser um for )

    print ' -\t%e\t%e\t%e\t%e' % (x0, x1, f(x1), flin(x0))
    for k in range(1, iterMax + 1):

        # # Em cada iteracao :
        # # Calcule x1 a partir de x0

        x1 = x0 - f(x0) / flin(x0)
        print ' -\t%e\t%e\t%e\t%e' % (x0, x1, f(x1), flin(x0))
        ab = f(x1)
        print '%d\t%e\t%e\t%e\t%e' % (k, x0, x1, f(x1), flin(x0))

    # # Teste para o criterio de parada usando modulo da funcao

        if abs(ab) < epsilon:
            return (False, x1)

        # # Atualize o valor de x0

        x0 = x1
        k = k + 1

        # # Se atingir o numero maximo de iteracoes mostra mensagem de erro e retorna
        # # a ultima raiz encontrada

    print ' ERRO ! numero maximo de iteracoes atingido .'
    return (True, x1)


    # # Inicializacao dos parametros

x0 = 2
epsilon = 0.1
iterMax = 50

## Chamando a funcao newton com os parametros definidos nas celulas acima

(houveErro, raiz) = newton(f, flin, x0, epsilon, iterMax)
if houveErro:
    print 'O Metodo retornou um erro .'
if raiz is not None:
    print ' Raiz encontrada : %s' % raiz


			