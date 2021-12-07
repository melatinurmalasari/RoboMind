mydoc = open('D:\\Notepad\chap10.2.txt', 'r')
#Direktori Dokumen
read = mydoc.readlines()
daftar = []
for data in range (len(read)):
    dataLama = read[data]
    dataBaru = dataLama.split('|')
    Dictionary = {'NIM' : dataBaru[0], 'Nama' : dataBaru[1], 'Alamat' : dataBaru[2]}
    daftar += [Dictionary]
print('Data Mahasiswa : ', daftar)

mydoc.close()