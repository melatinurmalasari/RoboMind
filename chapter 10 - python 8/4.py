mydoc = open('D:\\Notepad\chap10.2.txt', 'r')
#Direktori Dokumen
read = mydoc.readlines()
daftar = []
for data1 in range (len(read)):
    dataLama = read[data1]
    dataBaru = dataLama.split('|')
    Dictionary = {'NIM' : dataBaru[0], 'Nama' : dataBaru[1], 'Alamat' : dataBaru[2]}
    daftar += [Dictionary]
#Menggunakan script program sebelumnya
search = str(input('Masukkan NIM yang akan dicari : '))

while True:
    for data2 in daftar:
        if search == data2['NIM']:
            x = True
            for data2 in daftar:
                if search == data2['NIM']:
                    print('NIM     : ', data2['NIM'])
                    print('Nama    : ', data2['Nama'])
                    print('Alamat  : ', data2['Alamat'])
                    break
            break
        else:
            x = False
            for data2 in daftar:
                if search != data2['NIM']:
                    print('Data tidak ditemukan :(')
                    break
            break
        break
    break
                

mydoc.close()