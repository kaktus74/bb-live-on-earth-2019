import time

ruchy = 29 #wydajna liczba to 29 a przy liczbach wiekszych od ok 38 wynik jest ten sam z koncowka 895(wczesnie 894)
b = 1
c = 1
a = 1
e = 1
while ruchy > 1:
    c = a + b
    print(ruchy," ",c)
    a = b + c
    print(ruchy," ",a)
    b = c + a
    print(ruchy," ",b)
    ruchy = ruchy - 3
#    time.sleep(0.01)

e = b/a
print("wynik to", e,"moja dokładność(przez limit pythona) to 12 cyfr po przecinku.")
