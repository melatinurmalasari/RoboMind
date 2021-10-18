NameKar = input("Masukkan Nama Karyawan: ")
CodeKar = input("Masukkan Kode Karyawan: ")
Golkar = str(input("Masukkan Golongan     : "))
if (Golkar == "A") or (Golkar == "a"):
    GajiPokok = 10000000
    Potongan = 2.5
elif (Golkar == "B") or (Golkar == "b"):
    GajiPokok = 8500000
    Potongan = 2.0
elif (Golkar == "C") or (Golkar == "c"):
    GajiPokok = 7000000
    Potongan = 1.5
elif (Golkar == "D") or (Golkar == "d"):
    GajiPokok = 5500000
    Potongan = 1.0
else:
    print("Golongan Tidak Valid")

StatMenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

if (StatMenikah == 1):
    Status = "Menikah"
    TunjMenikah = 10 / 100 * GajiPokok
    JumAnak = int(input("Masukkan jumlah Anak  : "))
    TunjAnak = 5 / 100 * GajiPokok
    TunjAnak = TunjAnak * JumAnak

elif (StatMenikah == 2):
    Status = "Belum Menikah"
    TunjMenikah = 0
    TunjAnak = 0
    JumAnak = "-"

else:
    print("Status Menikah Tidak Valid")

GajiKotor = GajiPokok + TunjMenikah + TunjAnak
potongan = Potongan / 100 * GajiKotor
GajiBersih = GajiKotor - potongan

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("STRUK RINCIAN GAJI KARYAWAN")
print("*************************************")
print("Nama Karyawan    : " + NameKar + " (Kode : " + CodeKar + ")")
print("Golongan         : " + Golkar)
print("Status Menikah   : " + Status)
print("Jumlah Anak      : " + str(JumAnak))
print("#####################################")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Tunjangan Menikah: Rp.", int(TunjMenikah))
print("Tunjangan Anak   : Rp.", int(TunjAnak))
print("/////////////////////////////////////")
print("Gaji Kotor       : Rp.", int(GajiKotor))
print("Potongan (" + str(Potongan) + "%)  : Rp.", int(potongan))
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Gaji Bersih      : Rp.", int(GajiBersih))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")