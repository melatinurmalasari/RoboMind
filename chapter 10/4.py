mydoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\2.txt', 'r')

#Direktori Dokumen
baca = mydoc.readlines()
daftar = []
for data1 in range (len(baca)):
    dataLama = baca[data1]
    dataBaru = dataLama.split('|')
    Dictionary = {'NIM' : dataBaru[0], 'Nama' : dataBaru[1], 'Alamat' : dataBaru[2]}
    daftar += [Dictionary]
    
#Menggunakan script program sebelumnya
search = str(input('Silakan masukkan NIM yang ingin dicari : '))

while True:
    for datakedua in daftar:
        if search == datakedua['NIM']:
            x = True
            for datakedua in daftar:
                if search == datakedua['NIM']:
                    print('NIM     : ', datakedua['NIM'])
                    print('Nama    : ', datakedua['Nama'])
                    print('Alamat  : ', datakedua['Alamat'])
                    break
            break
        else:
            x = False
            for datakedua in daftar:
                if search != datakedua['NIM']:
                    print('Maaf data yang anda cari tidak dapat ditemukan :(')
                    break
            break
        break
    break
                

mydoc.close()