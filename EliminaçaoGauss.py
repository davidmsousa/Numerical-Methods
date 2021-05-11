#!/usr/bin/python
# -*- coding: utf-8 -*-


def escolhe_pivo(k, A, b):

    # # n sera a ordem da matriz A

    n = len(A)
    x = n * [0]
    y = n * [0]

    # # inicializa flag para controlar se houve troca de linha com false

    houve_troca = False

    # # identifica o elemento de maior valor absoluto e a linha onde ele esta iniciando variaveis

    i = 0
    linha = 0
    aux = 0
    j = 0
    j = k
    maior = A[k][k]
    while j < n - 2:
        if abs(A[j + 1][k]) > abs(A[j][k]):
            maior = A[j + 1][k]
            linha = j + 1

            # Auxiliar que contera o mesmo numero da linha
            # variavel auxiliar

            aux = linha
            houve_troca = True
        j = j + 1

    # Faz a troca das linhas

    if k != linha:
        while i < n:

            # y[i] sera um vetor auxiliar que sera usado para a troca

            y[i] = A[k][i]
            A[k][i] = A[linha][i]
            A[linha][i] = y[i]

            # Trocar valor para o vetor B

            x[k] = b[k]
            b[k] = b[linha]
            b[linha] = x[k]
            i = i + 1

    # # retorna a flag

    return houve_troca


def substituicoes_retroativas(A, b):

    # # n sera a ordem da matriz A

    n = len(A)

    # # inicializa o vetor x com tamanho n e elementos iguais a 0

    x = n * [0]

    # escreva o seu codigo aqui

    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    i = n - 2
    while i >= 0:
        j = i + 1

        # temp sera minha variavel auxiliar

        temp = b[i]
        while j < n:
            temp -= A[i][j] * x[j]
            j += 1
        x[i] = temp / A[i][i]
        i = i - 1
    return x


def gauss_pivot_det(A, b):

## n sera a ordem da matriz A

    n = len(A)

    # Escreva o seu codigo aqui
    # while (P<n):
    # variaveis auxiliar para pivotacao

    aux = 0
    pivot = 0
    p = 0

    # # Para cada etapa k

    i = 0
    while i < n - 1:

    # # ESCOLHER PIVO

        if p <= 1:
            pivot = escolhe_pivo(p, A, b)
            if pivot == True:
                aux = aux + 1
            p = p + 1
        j = i + 1

        # para cada linha

        while j < n:

            # # Calcula o fator m

            m = A[j][i] / A[i][i]
            contador = i
            while contador < n:

                # # Atualiza a linha i da matriz , percorrendo todas as colunas j

                A[j][contador] -= m * A[i][contador]
                contador = contador + 1

            # Atualiza o vetor b na linha i

            b[j] -= m * b[i]
            j = j + 1
        p = p + 1
        i = i + 1

    # # faz o calculo do determinante antes de chamar as substituicoes retroativas
    # escreva o seu codigo aqui DETERMINANTE

    x = substituicoes_retroativas(A, b)

    # Calcular DETERMINANTE

    h = 1

    # variavel auxiliar

    auxi = 1
    auxi = A[0][0] * auxi
    while h < n:
        auxi = A[h][h] * auxi
        det = auxi
        h = h + 1
    det = det * (-1) ** aux
    det = '{0:.2 f}'.format(det)
    return (x, det)


A = [[1, 2, 3], [3, 1, 0], [0, 3, 4]]
b = [3, 4, 3]
x = gauss_pivot_det(A, b)
print x

			