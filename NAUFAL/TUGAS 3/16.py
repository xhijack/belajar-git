x = int(input('masukan angka: '))
i = 0
hasil = 0
while i < x:
    i += 1
    if i**2 == x:
        print('bilangan perfect square')

if i**2 != x:
    print('bukan')