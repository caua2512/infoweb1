Quantia = int(input())
a = 1
b = 0
for i in range(Quantia):
 c = a + b
 a = b
 b = c
 if i == Quantia - 1:
   print(a)
 else:
   print(a, end=" ")
