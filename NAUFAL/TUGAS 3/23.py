x = int(input('masukan angka: '))
i = 1
while i <= x:
    y = 1
    while y <= x:
        print(i , ' ** ', y, '=', i**y)
        y += 1
    print('')
    i += 1