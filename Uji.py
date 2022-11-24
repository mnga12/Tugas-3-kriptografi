import random


def kuadratkali(basis, pangkat, mod):  # algoritma kuadratkali, menghitung a^n dalam mod m
    x = 1
    y = basis
    while pangkat > 0:
        if pangkat % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        pangkat //= 2
    return x


def jacobian(a, n):  # perhitungan simbol jacobi (a/n) dengan menggunakan sifat-sifat dari teori bliangan
    ans = 1
    while a:  # loop ini akan halt
        a = a % n  # sifat 1 dari Rosen 3rd ed. hlm 183
        if a == 1 or n == 1:
            return ans
        while a % 2 == 0 and a != 0:  # sifat 2 & 3
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                ans = -ans
        if a % 4 == 3 and n % 4 == 3:  # sifat 4
            ans = -ans
        if a == 0:
            return 0
        a, n = n, a
    return 0


def solovoystrassen(p, k):
    if p < 2:  # jelas bilangan bulat kurang dari 2 bukan bilangan prima
        return False
    if p != 2 and p % 2 == 0:  # jika p kelipatan 2 dan tidak sama dengan 2 maka p bukan prima
        return False
    for i in range(k):
        # generate bilangan random diantara 1 sampai p-1
        a = random.randint(1, p-1)
        jac = jacobian(a, p)
        mod = kuadratkali(a, (p - 1) // 2, p)
        if p - mod == 1:  # jika p-a = 1 maka a = -1 (mod p)
            mod = -1  # dalam modulo p
        if jac == 0 or mod != jac:  # teorema, jika p prima maka (a/p) = a^(p-1)/2 (mod p)
            return False
    return True


def test():  # untuk menguji suatu bilangan asli prima atau tidak
    n = int(input("n = "))
    k = 100
    if solovoystrassen(n, k):
        print(n, "mungkin prima")
    else:
        print(n, "komposit")


def search():  # mencari bilangan prima pada suatu selang
    a = int(input("batas bawah : "))
    b = int(input("batas atas : "))
    k = 100
    for i in range(a-1, b):
        if solovoystrassen(i, k):
            print(i, "mungkin prima")
