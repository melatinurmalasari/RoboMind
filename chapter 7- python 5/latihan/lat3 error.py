print("------------------------------------")
print(" PROGRAM HITUNG NILAI RATA-RATA ")
print("------------------------------------")

inputan = 0
PemBagi = 0
selesai = False
while not(selesai):
        try:
            dataTambah = int(input("Silakan masukkan bilangan bulat: "))
            inputan = inputan + dataTambah
            PemBagi += 1
            choice = None
            while choice not in("y","n"):
                choice = str(input("Tambah lagi (y/n)?: "))
                if(choice == "y"):
                    selesai = False
                elif(choice == "n"):
                    selesai = True
                else:
                    print("Tolong jawab pilihan (y/n)")
        except ValueError:
            print("Maaf ini bukan bilangan bulat")

print("Rata-ratanya adalah: {0}".format(inputan/PemBagi))