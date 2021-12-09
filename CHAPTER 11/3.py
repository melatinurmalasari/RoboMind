from datetime import*
from datetime import*
from datetime import*

def diffDate(x):
    tanggal = x.split("-")
    ListDate = []
    for i in tanggal:
        ListDate.append(int(i))
    ystrdy = date(ListDate[0], ListDate[1], ListDate[2])
    tdy = datetime.date(datetime.now())
    a = ystrdy - tdy
    b = a.days
    return b

file = open("DATA.MAHASISWA.txt", "r")
BacaFile = file.readlines()
kode = input("Silakan Memasukkan Kode Member Anda : ")
for i in range(len(BacaFile)):
    if(kode in BacaFile[i]):
        splitted = BacaFile[i].split("|")
        status = "Tersedia"
        break
    else :
        status = "Tidak Tersedia"
        continue

        
if(status == "Tersedia"):
    print("\nData Peminjam & pinjaman Buku")
    print("Kode Member Anda              : ", splitted[0])
    print("Nama Member Anda             : ", splitted[1])
    print("Judul Buku Yang Anda pinjam              : ", splitted[2])
    print("Tanggal Mulai Peminjaman buku : ", splitted[3])
    print("Tanggal Maks Peminjaman buku  : ", splitted[4])
    print("Tanggal Pengembalian buku    : ", datetime.date(datetime.now()))
    trlmbt = diffDate(splitted[4])
    denda = 2000 * abs(trlmbt)
    if(trlmbt >= 0):
        print("Terlambat : 0 hari")
        print("Denda : 0")
        
    else:
        print("Anda Terlambat : ", abs(trlmbt))
        print("Denda : ", denda)
        
else :
    print("Maaf data Peminjam & pinjaman anda Tidak Ditemukan")
