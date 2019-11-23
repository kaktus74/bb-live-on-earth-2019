import random
from random import randint
def kostka (liczba_rzutow, liczba_scianek):
    suma = 0
    for proba in range (0, liczba_rzutow):
        rzut = randint (1, liczba_scianek)
        print ('Wynik: ', rzut)
        suma = suma + rzut
    print ('Suma wyników to: ', suma)
    
