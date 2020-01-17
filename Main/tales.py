def tales (h1, p1, h2 = 400000):
    p2 = p1 * (h2 / h1)
    return p2

print(tales(1,1.5, 100000))

def co_ile (pole_widzenia_m, czas_obiegu_s = 5400, obwod_m = 40075000):
    ile_razy = obwod_m / pole_widzenia_m
    co_ile = czas_obiegu_s / ile_razy
    return co_ile

def dl_maly_bok (dlugi_bok, aspekt = 16/9):
    maly_bok = dlugi_bok  / aspekt
    return maly_bok