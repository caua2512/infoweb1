x = int(input())
y = int(input())
z = int(input())
def maior(x, y, z):
  maiorzin = x
 if x < y:
  maiorzin = y
  if x < z and y < z:
   maiorzin = z
  return maiorzin
print(maior(x,y,z))
