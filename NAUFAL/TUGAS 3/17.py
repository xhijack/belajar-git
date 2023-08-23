n = int(input('masukan angka prima: '))
i = 0
j = 1
while i < n:
    i += 1
    if (i == 1 or i == 2 or i == 3 or i == 5 or i == 7) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0) :
        print(i,end=' ')
    