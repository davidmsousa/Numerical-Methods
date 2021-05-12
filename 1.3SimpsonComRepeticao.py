import math

def fx(x):
    return (1 /(x**3 -2*x**2 + 5))


a = float(input("Primeiro valor do intervalo: "))
b = float(input("Segundo valor do intervalo: "))

while True:
    n = int(input("Número de divisões: "))
    if n % 2 == 0:
        break
    else:
        print("Entrada inválida, você deve entrar com uma número par")


h = (b -a)/n
firs = 0
secondSum = 0

for i in range(1, int(n / 2 + 1)):
    firs += fx(a + (2 * i -1) * h)

for i in range(1, int(n / 2)):
    secondSum += fx(a + (2 * i) * h)

integral = h / 3 * (fx(a) + fx(b) + 4 * firs + 2 * secondSum)
print("Integral definida da curva: ", integral)