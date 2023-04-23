tempo_de_viagem = int(input())
velocidade_media = int(input())

distancia_percorrida = velocidade_media * tempo_de_viagem
gasto = distancia_percorrida / 12

print(f'{gasto:.3f}')
