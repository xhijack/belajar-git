x = input('masukan angka: ')
jumlah = 0
z = 0
for i in x:
    z += 1

for i in x:
    int(i)
    jumlah += int(i)**z

if jumlah == x:
    print('bilangan armstrong')
else:
    print('bukan bilangan armstrong')