import time

enDoc = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\6.txt', 'r')

#Men-decrypt dokumen yang digunakan di program sebelumnya
encrypt = int(input('Masukkan sandi anda untuk decoding caesar (n) : '))
enText = list(enDoc.readline())

dcrypt = ''
for data in enText:
    if(data.isalpha()):
        Ascii       = ord(data)
        indexA      = Ascii - ord('A')
        newIndex    = (indexA - encrypt) % 26
        newpw       = newIndex + ord('A')
        caesar      = chr(newpw)
        dcrypt += caesar
    else:
        dcrypt += data

print('mohon tunggu, Sedang memecahkan kode.....')
time.sleep(3)
print('Sekarang, silakan priksa dokumen anda')

hasil = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\6a.txt', 'w')

#Direktori hasil output decrypt
hasil .tulis(dcrypt)
hasil .tutup()