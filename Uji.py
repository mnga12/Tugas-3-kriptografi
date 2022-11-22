import random


def kalikuadrat(basis, pangkat, mod):
    x = 1
    y = basis
    while pangkat > 0:
        if pangkat % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        pangkat //= 2
    return x


def jacobian(a, n):  # jacobian udah bener
    if a == 0:
        return 0
    ans = 1
    while a:
        a = a % n
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                ans = -ans
        if a % 4 == 3 and n % 4 == 3:  # sifat 4 tukar a dengan n, (a/n) = -(a/n) jika a=n=3 mod 4
            ans = -ans
        a, n = n, a
        if n == 1:
            return ans
    return 0


def solovoystrassen(p, k):
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    for i in range(k):
        # generate bilangan random diantara 1 sampai p-1
        a = random.randrange(p - 1) + 1  # random.randrange(a) akan memberikan sebuah bilangan random bulat dari 0 sampai a-1.
        hasil = jacobian(a, p)
        mod = kalikuadrat(a, (p - 1)//2, p)
        if p-mod == 1:
            mod = -1
        print(a,hasil,mod)
        if hasil == 0 or mod != hasil:
            return False
    return True

def main():
  n = int(input("n = "))
  k = 100
  if solovoystrassen(n,k):
    print(n, "prima")
  else:
    print(n, "komposit")

main()
