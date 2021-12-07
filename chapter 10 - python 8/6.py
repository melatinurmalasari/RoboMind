import time

tAsli = str(input('Masukkan data yang akan di-enkripsi     : '))
#Kalimat yang akan dienkripsi (Huruf Kapital)
pw = int(input('Mohon masukkan kode enkripsi Caesar (n) : '))
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

print('Sedang mengenkripsi.....')
time.sleep(3)
print('Silahkan periksa dokumen terkait')

result = open('D:\\Notepad\chap10.caesar.txt', 'w')
#Direktori hasil output
result.write(dcrypt)
result.close()