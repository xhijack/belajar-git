x = int(input('masukan angka: '))
i = 0
jumlah = 1
while i < x:
    i += 1
    jumlah *= i
    print(i,end=' ')
    if i < x:
        print('x', end=' ')

print('=', jumlah,end='')