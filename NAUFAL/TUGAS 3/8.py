x = int(input('masukan angka: '))
i = 0
angka = 0
while i < x:
    i += 1
    if x % i == 0:
        angka += 1

if angka == 2:
    print('bilangan prima')
else:
    print('bukan bilangan prima')