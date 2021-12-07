import time

tAsli = str(input('Silakan masukkan data yang akan di-enkripsi     : '))
#Kalimat yang akan dienkripsi (Huruf Kapital)
pw = int(input('Mohon segera masukkan kode enkripsi Caesar (n) : '))
teks = list(tAsli)

dcrypt = ''
for data in teks:
    if(data.isalpha()):
        Ascii       = ord(data)
        indexA      = Ascii - ord('A')
        newIndex    = (indexA + pw) % 26
        newpw       = newIndex + ord('A')
        caesar      = chr(newpw)
        dcrypt += caesar
    else:
        dcrypt += data

print('Tunggu Saat ini sedang mengenkripsi.....')
time.sleep(3)
print('Silahkan periksa dokumen ysng dibutuhkan')

result = open('C:\\user\Melati Nur Malasari\Document\chapter 10 - python 8\6.txt', 'w')

#Direktori hasil output
result.write(dcrypt)
result.close()