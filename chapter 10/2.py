mahasiswaNim = []
mahasiswaNama = []
mahasiswaAlamat = []
i = 0

while True:
    nim     = str(input('Silakan Masukan NIM      : '))
    nama    = str(input('Silakan Masukan Nama MHS : '))
    alamat  = str(input('Silakan Masukan Alamat   : '))
    mahasiswaNim += [nim]
    mahasiswaNama += [nama]
    mahasiswaAlamat += [alamat]
    
    loop   = str(input('\nIngin Input Data Lagi? (y/n) : '))
    if (loop == 'y'):
        continue
    else:
        break
    i += 1

mydoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\2.txt', 'w')
#Lokasi Direktori Dokumen
for data in range (len(mahasiswaNim)):
    i = (mahasiswaNim[data]+'|'+mahasiswaNama[data]+'|'+mahasiswaAlamat[data])
    mydoc.write(i)
    mydoc.write('\n')
mydoc.close()
print('\nDimohon Segera Periksa Dokumen Terkait\n')