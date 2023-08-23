y = int(input('masukan angka: '))
i = 0
jumlah = 1
hasil = 1
while i < y:
    i += 1
    jumlah *= i
    hasil += jumlah
    print(jumlah)