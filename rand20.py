import secrets

b = 0
x = []

def makerand():
    b = 0
    x = list(range(0, 20))
    while (b < 20):
        x[b] = (secrets.randbits(8))
        b = b + 1
    return x