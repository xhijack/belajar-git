x = int(input('masukan angka: '))
y = int(input('masukan angka: '))
z = int(input('masukan angka: '))
if x == y and x == z and y == z:
    print('segitiga sama sisi')
elif x == y or x == z or y == z:
    print('segitiga sama kaki')
else:
    print('segitiga tak beraturan')