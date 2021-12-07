import time
try:
    mydoc = open('D:\\Notepad\chap10.3.txt', 'r')
    #Direktori Dokumen
    data1 = mydoc.readlines()
    x = 0
    data2 = []
    for  i in data1:
        bil = str(data1[x])
        bil = bil.split('|')
        data2.append(bil)
        x += 1
    mydoc.close()

    newdoc = open('D:\\Notepad\chap10.3a.txt', 'w')
    #Direktori Dokumen
    y = 0
    for angka in data2:
        bil1 = int(data2[y][0])
        bil2 = int(data2[y][1])
        newdoc.write(str(bil1+bil2) + '\n')
        y += 1
    newdoc.close()
    print('Sedang menghitung.......')
    time.sleep(3)
    print('SUKSES! Silahkan periksa dokumen terkait')
        
except FileNotFoundError:
    print('File tidak ditemukan :(')
