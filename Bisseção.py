import math


def f(x):
    return math.cosh(x) * math.cos(x)


def bissecao(f, a, b, epsilon, maxIter=12):
    """Executa o método da bisseção para achar o zero de f no intervalo
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    # Inicializar as variáveis Fa e Fb
    Fa = f(a)
    Fb = f(b)

    # Teste para saber se a função muda de sinal. Se não mudar, mostrar
    # mensagem de erro
    if ((f(a)*f(b)) < 0):
        print("Sem Erros !!!")
    else:  # Mostrar mensagem
        print("Erro! A função não muda de sinal.")
        return (True, None)

    # Mostra na tela cabeçalho da tabela
    print("k\t\t   a\t\t\t  fa\t\t\t   b\t\t\t   fb\t\t\t  x\t\t\t    fx\t\t\t  intervX")

    # Inicializa tamanho do intervalo intervX usando a função abs, x e Fx
    intervX = abs(b-a)
    x = abs(b-a)
    Fx = f(x)

    # Mostra dados de inicialização
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, Fa, b, Fb, x, Fx, intervX))

    # Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    # escreva o seu código aqui
    if(intervX < 0.001):
        return intervX


    # Iniciliza o k
    # escreva o seu código aqui
    k = 1
    fb = f(b)
    fa = f(a)
    # laço

    while k <= maxIter:
        # Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        # as variáveis apropriadamente
        # escreva o seu código aqui
        x = (a + b) / 2
        if((f(a)*f(x)) < 0):
            b = x
            fb = f(x)
        else:
            a = x
            fa = f(x)

    # Atualiza intervX, x, e Fx
        x = ((a+b)/2)
        Fx = f(x)
        Fa = f(a)
        Fb = f(b)
        intervX = (b-a)
    # Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e" %
              (k, a, Fa, b, Fb, x, Fx, intervX))

    # Teste do critério de parada (usando apenas o tamanho do intervalo)
    # escreva o seu código aqui
        if((intervX) < 0.001):
            break

    # Atualiza o k
        k = k + 1
    # Se chegar aqui é porque o número máximo de iterações foi atingido
    # Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return(True, x)


print(f(0))

a = 4
b = 5
epsilon = 0.0001
maxIter = 12


(houveErro, raiz) = bissecao(f, a, b, epsilon, maxIter)


if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)
