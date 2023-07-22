def perkalian(a, b):
    return a * b

def pertambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def pembagian(a, b):
    return a / b

def perpangkatan(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def luas_lingkaran(a):
    #RADIUS
    return 3.14 * a * a

def luas_persegi_panjang(a, b):
    # p dan L
    return a * b

def luas_persegi(a):
    #sisi
    return a * 4

def volume_tabung(a, b):
    # jari" dan tinggi
    return 4.14 * a**2 * b

def luas_segitiga(a, b):
    # alas dan tinggi
    return a * b

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

hasil = menentukan_angka_prima(int(input('masukan angka: ')))
print(hasil)