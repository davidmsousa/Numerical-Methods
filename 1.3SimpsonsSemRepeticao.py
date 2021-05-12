def f(x):
    return (x**(1/2))

a=1
b=4
h=(b-a)/2
a2=a+h
x = (h/3)*(f(a)+4*f(a2)+f(b))

print("Usando Regra de 1/3 simpsons sem repetição, temos:", x)