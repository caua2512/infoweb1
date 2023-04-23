n = int(input())
for i in range(1,n+1):
  linha1 = input().split()
  x = int(linha1[0])
  y = int(linha1[1])
  if y == 0:
    print('divisao impossivel')
  if y != 0:
    divisão = x/y
    print(f'{divisão:.1f}')
