mhsNim = []
mhsNama = []
mhsAlamat = []
i = 0

while True:
    nim     = str(input('Masukan NIM      : '))
    nama    = str(input('Masukan Nama MHS : '))
    alamat  = str(input('Masukan Alamat   : '))
    mhsNim += [nim]
    mhsNama += [nama]
    mhsAlamat += [alamat]
    
    loop   = str(input('\nMau Input Data Lagi? (y/n) : '))
    if (loop == 'y'):
        continue
    else:
        break
    i += 1

mydoc = open('D:\\Notepad\chap10.2.txt', 'w')
#Lokasi Direktori Dokumen
for data in range (len(mhsNim)):
    i = (mhsNim[data]+'|'+mhsNama[data]+'|'+mhsAlamat[data])
    mydoc.write(i)
    mydoc.write('\n')
mydoc.close()
print('\nSilahkan Periksa Dokumen Terkait\n')