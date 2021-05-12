def f(x):
    return (1 -x -4*x**3 + 2*x**5)

def trap(a,b,m):
    x=(m+1)*[0]
    h=b-a #intervalo
    p=h/m 
    s=0
    i=0
    while i<=m:
        if(i==0):
            x[0]=a
        else:
            x[i]=x[i-1] + p
        i=i+1
    i=1
    while(i<=(m-1)):
        s+=f(x[i])
        i=i+1
    trap = ((p/2)*(f(x[0])+2*s+f(x[m]))) #Com repetição
    return trap

#SEM REPETIÇÃO 
a=-2
b=4
h=b-a
x = (h/2)*(f(a)+f(b))
print("\nUsando Regra do trapezio sem repetição, temos:", x)

#COM REPETIÇÃO
m=3
print("Número de repetições: ",m)
z=trap(a,b,m)
print("Usando regra do trapezio com repetições, temos: ",z)