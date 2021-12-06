try:
    mydoc = open('D:\\Notepad\chap10.1.txt', 'r')
    #Merupakan direktori dimana saya menyimpan file txt
    bil = mydoc.readlines()
    genap = 0
    ganjil = 0
    i = 0

    try:
        while True:
            value = int(bil[i])
            if (value % 2 == 0):
                genap += 1
            if (value % 2 != 0):
                ganjil += 1
            i += 1
        
            if not bil:
                break
    except IndexError:
        print('')
except FileNotFoundError:
    print('File Tidak Ditemukan :(')

print('Jumlah bilangan genap dalam data adalah   : ', genap)
print('Jumlah bilangan ganjil dalam data adalah  : ', ganjil)

mydoc.close()