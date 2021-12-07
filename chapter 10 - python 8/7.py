import time

enDoc = open('D:\\Notepad\chap10.caesar.txt', 'r')
#Men-decrypt dokumen yang digunakan di program sebelumnya
encrypt = int(input('Masukkan sandi untuk decoding caesar (n) : '))
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

print('Sedang memecahkan kode.....')
time.sleep(3)
print('Silahkan periksa dokumen terkait')

result = open('D:\\Notepad\chap10.caesar2.txt', 'w')
#Direktori hasil output decrypt
result.write(dcrypt)
result.close()