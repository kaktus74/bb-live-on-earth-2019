import random
from random import randint
def main ():
    liczba_scianek = int (input ('Ile ścianek ma twoja kostka? '))
    liczba_rzutow = int (input ('Ile razy chcesz rzucić? '))
    suma = 0
    for proba in range (0, liczba_rzutow):
        rzut = randint (1, liczba_scianek)
        print ('Wynik: ', rzut)
        suma = suma + rzut
    print ('Suma wyników to: ', suma)

if __name__ == '__main__':
    main ()

    
    
