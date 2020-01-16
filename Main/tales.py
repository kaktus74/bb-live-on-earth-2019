def tales (h1, p1, h2=400000):
    p2 = p1 * (h2 / h1)
    return p2

print(tales(1,1.5, 100000))
