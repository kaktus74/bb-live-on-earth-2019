import random
from random import randint
def main ():
    ilosc_scianek = (int ('Ile ścianek ma twoja kostka? '))
    ilosc_rzutow = (int ('Ile razy chcesz rzucić? '))
    suma = 0
    for proba in range (0, liczba_rzutow):
        rzut = randint (1, liczba_scianek)
        print ('Wynik: ', rzut)
        suma = suma + rzut
    print ('Suma wyników to: ', suma)

if __name__ == '__main__':
    main ()

    
    
