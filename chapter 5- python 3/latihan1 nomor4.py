NameKar = input("Masukkan Nama Karyawan: ")
CodeKar = input("Masukkan Kode Karyawan: ")
Golkar = str(input("Masukkan Golongan     : "))
if (Golkar == "A") or (Golkar == "a"):
    GajiPokok = 10000000
    Persen = 2.5

elif (Golkar == "B") or (Golkar == "b"):
    GajiPokok = 8500000
    Persen = 2.0

elif (Golkar == "C") or (Golkar == "c"):
    GajiPokok = 7000000
    Persen = 1.5

elif (Golkar == "D") or (Golkar == "d"):
    GajiPokok = 5500000
    Persen = 1.0

else:
    print("Golongan tidak valid")

GajiKotor = Persen / 100 * GajiPokok
GajiBersih = GajiPokok - GajiKotor

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("STRUK RINCIAN GAJI KARYAWAN")
print("************************************")
print("Nama Karyawan    : " + NameKar + " (Kode : " + CodeKar + ")")
print("Golongan         : " + Golkar)
print("####################################")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Potongan (" + str(Persen) + "%)  : Rp.", int(GajiKotor))
print("////////////////////////////////////")
print("Gaji Bersih      : Rp.", int(GajiBersih))