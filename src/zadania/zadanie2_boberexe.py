import random


n=int(input('ile rzutów'))
suma=0
q=1
while q<=n:
    punkty = random.randint(1,6)
    suma = punkty + suma
    print('rzut',q,'wynik: ',punkty)
    q=q+1


print('=-=-=-=-=-=-=')
print('Suma :' , suma)