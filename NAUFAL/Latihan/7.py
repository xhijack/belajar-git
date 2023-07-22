# 1
def perkalian(a, b):
    return a * b
# 2
def pertambahan(a, b):
    return a + b
# 3
def pengurangan(a, b):
    return a - b
# 4
def pembagian(a, b):
    return a / b
# 5
def perpangkatan(a, b):
    return a ** b
# 6
def modulus(a, b):
    return a % b
# 7
def luas_lingkaran(a):
    #RADIUS
    return 3.14 * a * a
# 8
def luas_persegi_panjang(a, b):
    # p dan L
    return a * b
# 9
def luas_persegi(a):
    #sisi
    return a * 4
# 10
def volume_tabung(a, b):
    # jari" dan tinggi
    return 4.14 * a**2 * b
# 11
def luas_segitiga(a, b):
    # alas dan tinggi
    return a * b
# 12
def menentukan_angka_prima(a):
    i = 0
    angka = 0
    while i < a:
        i += 1
        if a % i == 0:
            angka += 1
    if angka == 2:
        return 'bilangan prima'
    else:
        return 'bukan bilangan prima'
# 13
def fibonacci(a):
    x, y = 0, 1
    while y < a:
        x, y = y, x + y
    if y == x:
        return "Angka tersebut adalah bilangan Fibonacci"
    else:
        return "Angka tersebut bukan bilangan Fibonacci"
# 14
def armstrong(a):
    jumlah = 0
    z = 0
    for i in str(a):
        z += 1
        return
# 15
    for i in str(a):
        int(i)
        jumlah += int(i)**z
        return

# 16
    if jumlah == a:
        return 'bilangan armstrong'
    else:
        return 'bukan bilangan armstrong'
# 17
def menentukan_bilangan_neg_pos(a):
    if a > 0:
        return 'Positive'
    else:
        return 'Negative'
#18
def luas_lingkaran(a):
    return 3.14 * a * a

# def luas_persegi_panjang(a, b):
#     # p dan L
#     return a * b

# def luas_persegi(a):
#     #sisi
#     return a * 4

# def luas_lingkaran(a):
#     RADIUS
#     return 3.14 * a * a

# def luas_persegi_panjang(a, b):
#     p dan L
#     return a * b

# def luas_persegi(a):
#     sisi
#     return a * 4

# def perkalian(a, b):
#     return a * b

# def pertambahan(a, b):
#     return a + b

# def pengurangan(a, b):
#     return a - b

# def pembagian(a, b):
#     return a / b

# def perpangkatan(a, b):
#     return a ** b

# def modulus(a, b):
#     return a % b

# def luas_lingkaran(a):
#     #RADIUS
#     return 3.14 * a * a

# def luas_persegi_panjang(a, b):
#     # p dan L
#     return a * b

# def luas_persegi(a):
#     #sisi
#     return a * 4

while 1 > 0:
    x = int(input('''
1
2              
3              
4              
5              
6              
7              
8              
9              
10              
11              
12              
13              
14              
15              
16              
17              
18              
19              
20              
21              
22              
23              
24              
25              
26              
27              
28              
29              
30              
              
pilih salah satu dari 1 sampai 30: '''))
    