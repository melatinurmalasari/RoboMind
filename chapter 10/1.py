try:
    mydoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\1.txt', 'r')
    #Merupakan direktori dimana saya menyimpan file txt
    bil = mydoc.readlines()
    bilgenap = 0
    bilganjil = 0
    i = 0

    try:
        while True:
            value = int(bil[i])
            if (value % 2 == 0):
                bilgenap += 1
            if (value % 2 != 0):
                bilganjil += 1
            i += 1
        
            if not bil:
                break
    except IndexError:
        print('')
except FileNotFoundError:
    print('File Tidak Ditemukan :(')

print('berapa Jumlah bilangan genap yang terdapat dalam data   : ', bilgenap)
print('berapa Jumlah bilangan ganjil yang terdapat dalam data  : ', bilganjil)

mydoc.close()