maior = 0
posiçao = 0
for i in range(100):
  numero = int(input())
  if numero>maior:
    maior = numero
    posiçao = i

print(maior)
print(posiçao + 1)
