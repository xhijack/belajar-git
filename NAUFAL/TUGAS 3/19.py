x = int(input('masukan angka: '))
y = int(input('masukan angka: '))
i = 0
j = 0
while i < x or j < y:
    i += 1
    j += 1
    if (i == 1 or i == 2 or i == 3 or i == 5 or i == 7) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0) :
        if i < x:
            print(i, end=' ')
        if j < y:
            print(j, end=' ')
        print()