import random
n = int(input('Ile rzutów?'))
suma = 0
k = 1
while k<=n:
    wynik = random.randint(1,6)
    suma = suma + wynik
    print('Rzut ',k ,', wynik  : ', wynik)
    k = k + 1

print('------------')
print('Suma wyników  : ', suma)