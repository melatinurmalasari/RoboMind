mydoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\2.txt', 'r')
#Direktori Dokumen
baca = mydoc.readlines()
daftar = []
for data in range (len(baca)):
    dataLama = baca[data]
    dataBaru = dataLama.split('|')
    Dictionary = {'NIM' : dataBaru[0], 'Nama' : dataBaru[1], 'Alamat' : dataBaru[2]}
    daftar += [Dictionary]
print('Data Mahasiswa : ', daftar)

mydoc.close()