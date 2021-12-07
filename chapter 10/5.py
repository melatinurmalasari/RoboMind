import time
try:
    mydoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\5.txt', 'r')

    #Direktori Dokumen
    dataSATU = mydoc.readlines()
    x = 0
    datakedua = []
    for  i in dataSATU:
        bil = str(dataSATU[x])
        bil = bil.split('|')
        datakedua.append(bil)
        x += 1
    mydoc.close()

    newdoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\5a.txt', 'w')

    #Direktori Dokumen
    y = 0
    for angka in datakedua:
        bil1 = int(datakedua[y][0])
        bil2 = int(datakedua[y][1])
        newdoc.write(str(bil1+bil2) + '\n')
        y += 1
    newdoc.close()
    print('Mohon menunggu proses sedang berjalan.......')
    time.sleep(3)
    print('SUKSES! Silahkan periksa dokumen yang di cari')
        
except FileNotFoundError:
    print('Maaf file yang anda cari tidak ditemukan :(')
