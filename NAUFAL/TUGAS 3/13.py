x = int(input('masukan angka: '))
a = 0
b = 1
while b < x:
    a, b = b, a + b
    print(a)