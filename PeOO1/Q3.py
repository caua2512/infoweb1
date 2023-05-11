class viagem:
  def __init__(self):
    self.Dist = 0
    self.hrs = 0
  def calc_velocidade_media(self):
    return self.dist / self.hrs
x = viagem()
x.dist = int(input())
x.hrs = float(input())
print(x.calc_velocidade_media())
