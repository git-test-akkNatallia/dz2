print('Write the number a = ')
a = int(input())
print('Write the number b = ')
b = int(input())
print(a % b)


print('Write the number k = ')
k = int(input())
print('Write the number q = ')
q = int(input())
print(q > k)
if q > k:
    print(max(k,q))


print('Write the number g = ')
g = int(input())
print('Write the number r = ')
r = int(input())

kol = 0
while g > 0:
    ew = g % 10
    kol = kol + 1
    g = g // 10

kol1 = 0
while r > 0:
    rew = g % 10
    kol1 = kol1 + 1
    r = r // 10

if kol1 > kol:
    print(max(kol, kol1))



print('Write the number n = ')
n = int(input())
print('Write the number f = ')
f = int(input())
print('large sum of digits')
suma = 0
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
suma1 = 0
while f > 0:
    we = f % 10
    suma1 = suma1 + we
    f = f // 10
if suma > suma1:
    print(max(suma,suma1))