import secrets

b = 0

while b < 20:
    print(secrets.randbits(8))
    b = b + 1