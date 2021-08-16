import math

primeiro_x = int(input('Digite um número: '))
primeiro_y = int(input('Digite um número: '))
segundo_x = int(input('Digite um número: '))
segundo_y = int(input('Digite um número: '))

distancia = sqrt((primeiro_x - segundo_x)**2 + (primeiro_y - segundo_y)**2)

if distancia >= 10:
    print('longe')
else:
    print('perto')