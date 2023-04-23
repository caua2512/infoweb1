parte1 = input().split()
X = float(parte1[0])
Y = float(parte1[1])
Z = float(parte1[2])

pi = 3.14159
pi = float(pi)
A1 = X * Z / 2
A2 = Z ** 2 * pi
A3 = (X + Y) * Z / 2
A4 = Y ** 2
A5 = X * Y

print(f'TRIANGULO: {A1:.3f}')
print(f'CIRCULO: {A2:.3f}')
print(f'TRAPEZIO: {A3:.3f}')
print(f'QUADRADO: {A4:.3f}')
print(f'RETANGULO: {A5:.3f}')
