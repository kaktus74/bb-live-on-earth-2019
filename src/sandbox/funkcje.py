#def odejmuj(a,b):
#    return  a - b
#a = 10
#b = 5
#print(odejmuj(b=12,a=34))

def na_ulamki(x):
    x = [str(i) for i in x]
    x [0] += '/1'
    x [1] += '/1'
    x [2] += '/10'
    " ".join(x)
    return x

x = [6 ,8 ,9.5]