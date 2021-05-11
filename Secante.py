#!/usr/bin/python
# -*- coding: utf-8 -*-


def f(x):
    return x ** (4 / 3) - 4


def secante(
    f,
    x0,
    x1,
    epsilon,
    iterMax=50,
    ):

# Executa o metodo da Secante para achar o zero de f
# a partir das aproximacoes x0 e x1 , e da tolerancia
# epsilon .
# Retorna uma tupla ( houveErro , raiz ), onde houveErro e
# booleano .

    print 'k\t\tx2\t\t\t\tf(x2)'
    k = 1.0
    x2 = 1
    print ' -\t%e\t%e' % (x2, f(x2))

    # # Inicie as iteracoes

    while k <= iterMax:

        # # Em cada iteracao :
        # # Calcule x2 a partir de x0 e x1

        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

        # # Teste para o criterio de parada usando modulo da funcao

        print '%d\t%e\t%e' % (k, x2, f(x2))
        if abs(f(x2) < epsilon):
            return (False, x2)

    # # Atualize os valores de x0 e x1

        x0 = x1
        x1 = x2
        k = k + 1

    # # Se atingir o numero maximo de iteracoes mostra mensagem de erro e retorna

    print ' ERRO ! numero maximo de iteracoes atingido .'
    return (True, x2)


## Inicializacao dos parametros

x0 = 3
x1 = 2
epsilon = 0.01
iterMax = 50
(houveErro, raiz) = secante(f, x0, x1, epsilon, iterMax)

if houveErro:
    print 'O Metodo retornou um erro .'
if raiz is not None:
    print ' Raiz encontrada : %s' % raiz

			