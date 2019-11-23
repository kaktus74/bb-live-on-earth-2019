import random
from random import randint
def kostka (ilosc_rzutow, liczba_scianek):
    suma = 0
    for i in range (0, ilosc_rzutow):
        x = randint (1, liczba_scianek)
        print ('Wynik: ', x)
        suma = suma + x
    print ('Suma wyników to: ', suma)
    
