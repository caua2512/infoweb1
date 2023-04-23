n = int(input())
c = 0
r = 0
s = 0
for i in range(1, n+1):
 x = input().split()
 if x[1] == 'C':
   c = c + int(x[0])
 if x[1] == 'S':
   s = s + int(x[0])
 if x[1] == 'R':
   r = r + int(x[0])

total = c + r + s
pc = (c/total) * 100
pr = (r/total) * 100
ps = (s/total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')
