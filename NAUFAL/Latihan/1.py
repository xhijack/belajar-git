x = int(input('nilai harta : '))
y = int(input('nilai emas : '))
if x > y*85:
    z = input('sudah masuk haul YA/TIDAK: ')
    if x > y*85 and z == 'YA':
        x *= 0.025
        print('zakat yang harus di bayar : ', x)
else:
    print('harta belum bisa di zakatkan')