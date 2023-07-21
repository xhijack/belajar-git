x = float(input('masukan tahun: '))
if x >= 400:
    if x % 4 == 0 and x % 400 == 0:
        print('abad kabisat')
    elif x % 4 == 0:
        print('tahun kabisat')
    else:
        print('bukan tahun dan abad kabisat')
elif x < 100:
    if x % 4 == 0 :
        print('tahun kabisat')
    else:
        print('bukan tahun kabisat')