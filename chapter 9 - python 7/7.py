mahasiswa = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
            'K002:MELATI NUR MALASARI:2001-11-13:KLATEN',
            'K003:SYAHRANI DEVI KUMALASARI:2007-12-28:KUANSING']

print('='*65)
print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(25),'TANGGAL LAHIR'.ljust(20),'TEMPAT LAHIR')
print('-'*65)

for Isi in mahasiswa:
    isiSplit = Isi.split(':')
    NIM = isiSplit[0]
    Nama = isiSplit[1]
    TanggalLahir = isiSplit[2]
    TanggallahirSplit = TanggalLahir.split('-')
    Tanggal = TanggallahirSplit[2]
    Bulan = TanggallahirSplit[1]
    Tahun = TanggallahirSplit[0]
    TempatLahir = isiSplit[3]
    print(NIM.ljust(10),Nama.ljust(25),Tanggal,'/',Bulan,'/', Tahun.ljust(10),TempatLahir)
print('='*65)