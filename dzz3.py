a = 123556
b = 344
print(a % b)



import math
k = 2870345
q = 2870349
if q > k:
    print(max(k,q))


n = 47
suma = 0
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10

f = 235
suma1 = 0
while f > 0:
    we = f % 10
    suma1 = suma1 + we
    f = f // 10
if suma > suma1:
    print(max(suma,suma1))


g = 762232
kol = 0
while g > 0:
    ew = g % 10
    kol = kol + 1
    g = g // 10

r = 2433637801
kol1 = 0
while r > 0:
    rew = g % 10
    kol1 = kol1 + 1
    r = r // 10

if kol1 > kol:
    print(max(kol, kol1))