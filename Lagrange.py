def Lagrange(V,n):
    L = n * [0]
    Pn = 0
    i = 0
    while (i < n):# ordem
        L[i] = 1
        j = 0
        while (j < n):
            if (j != i):
                L[i] = L[i] * ((V -x[j]) / (x[i] -x[j]))
            j = j + 1
        Pn = Pn + L[i] * y[i]
        i = i + 1
    return Pn

V=3.4 #VALOR QUE QUERO ACHAR
x=(2.5,3,4)
y=(6.5,7,3)
n=len(x) #ORDEM
z = Lagrange(V,n)
print("\nOrdem da interpolação será de grau",(n-1))
print("O valor que quero descobrir será:",V )
print("O valor de f(",V,") será: ",z)