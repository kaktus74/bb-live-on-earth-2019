
import random


def main():
	n = int(input("Ile rzutow?"))
	i = 1
	suma = 0
	while i <= n:
		rzut = random.randint(1,6)
		suma = suma+rzut
		print('Rzut ', i, ', wynik : ', rzut)
		i = i + 1
	print("===============")
	print(suma)	
	zzz = input("\n\nAby zakonczyc program, kliknij Enter");
	

if __name__ == "__main__":
	main()

