import random


def kalikuadrat(basis, pangkat, mod):
    x = 1
    y = basis
    while pangkat > 0:
        if pangkat % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        pangkat //= 2
    return x % mod


def jacobian(a, n):
    if a == 0:
        return 0  # (0/n) = 0
    ans = 1
    if a < 0:
        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if n % 4 == 3:
            # (-1/n) = -1 jika n = 3 (mod 4)
            ans = -ans
    if a == 1:
        return ans  # (1/n) = 1
    while a:
        if a < 0:
            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if n % 4 == 3:
                # (-1/n) = -1 jika n = 3 (mod 4)
                ans = -ans
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                ans = -ans
        # tukar a dengan n
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            ans = -ans
        a = a % n
        if a > n // 2:
            a = a - n
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
        hasil = (p + jacobian(a, p)) % p
        mod = kalikuadrat(a, (p - 1) / 2, p)
        if hasil == 0 or mod != hasil:
            return False
    return True


def main():
    n = int(input("n = ")
    k = int(input("jumlah iterasi yang dilakukan = "
    if solovoystrassen(n,k):
        print(n, "prima")
    else:
        print(n, "komposit")


main()
