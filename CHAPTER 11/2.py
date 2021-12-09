from datetime import datetime
from datetime import date
from datetime import timedelta


try:
    myDoc = open('DATA.MAHASISWA.txt', 'a')
    Daftar = []
    loop = 'y'
    while True:
        KodeMember = input('Silakan untuk memasukkan Kode Member anda : ')
        NamaMember = input('Silakan untuk memasukkan Nama Member anda : ')
        JudulBuku   = input('Silakan untuk memasukkan Judul Buku yang anda cari : ')
        dateOne = datetime.date(datetime.now())
        dateTwo = dateOne + timedelta(days=7)
        Masuk = KodeMember+'|'+NamaMember+'|'+JudulBuku+'|'+str(dateOne)+'|'+str(dateTwo)
        Daftar.append(Masuk)
        loop = input('Ingin menambah data lagi? (y/n) : ')
        if loop == 'y':
            continue
        else:
            break

    n = 0
    for data in Daftar:
        peminjaman = str(Daftar[n])
        myDoc.write(peminjaman+'\n')
        n += 1

    myDoc.close()


except FileNotFoundError:
    print('Maaf File yang ingin anda cari tidak dapat ditemukan :(')