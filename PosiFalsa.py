import math

def f(x):
    return math.cosh(x) * math.cos(x)

def false_pos(f, a, b, epsilon, maxIter=50):
    Fa = f(a)
    Fb = f(b)

    if ((f(a) * f(b)) < 0):
        print("Sem Erros !!!")
    else:
        print("Erro! A fun��o n�o muda de sinal.")
        return (True, None)

    intervX = abs(b - a)
    if (intervX < 0.001):
        return intervX
    if (f(a)==0):
        return a
    if (f(b)==0):
        return b

    print("k\t     a\t\t       Fa\t\t       b\t\t       Fb\t\t      x\t\t\t      Fx\t\t       intervX")

    Fa=f(a)
    Fb=f(b)

     for k in range(1, maxIter + 1):
        x = (abs(a*Fb - b*Fa)/abs(Fb - Fa))
        Fx = f(x)

        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, Fa, b, Fb, x, Fx, intervX))

        if (abs(Fx) < abs(epsilon)):
            break
        if((f(a)*f(x)) < 0):
            b=x
            fb = f(x)
        else:
            a=x
            fa= f(x)

        x= ((a*Fb - b*Fa)/(Fb - Fa))
        Fx=f(x)
        Fa=f(a)
        Fb=f(b)
        intervX=(abs(a-b))

        if (intervX<(epsilon)):
            break

    print("ERRO! n�mero m�ximo de itera��es atingido.")
    return (True, x)

a = 4
b = 5
epsilon = 0.001
maxIter = 20


(houveErro, raiz) = false_pos(f, a, b, epsilon, maxIter)

if houveErro:
    print("O M�todo da Posi��o Falsa retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s" % raiz)
