def f(x):
    return (1 /(x**3 -2*x**2 + 5))

a=1
b=5
h=(b-a)/3
a2=a+h
a3=a2+h
x = (3*h/8)*(f(a)+3*f(a2)+3*f(a3)+f(b))
print("\nUsando Regra de 3/8 de simpson, temos:", x)