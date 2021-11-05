namaFile = str(input("Masukkan nama file: "))
namaFile = "C:\Users\Melati Nur Malasari\Documents\chapter 7\latihan\contohfile.txt"
try:
    selesai = False
    while not(selesai):
        dataTambah = str(input("Data yang ingin anda tambahkan: "))
        f = open(namaFile, "a")
        f.write("{0}\n".format(dataTambah)) # I dont know why a not make a new line
        f.close()
        choice = None
        while choice not in("y","n"):
            choice = str(input("Mau lagi (y/n)?: "))
            if(choice == "y"):
                selesai = False
            elif(choice == "n"):
                selesai = True
            else:
                print("Tolong jawab pilihan (y/n)")

except FileNotFoundError:
    print("File anda tidak ditemukan, apakah lokasi file anda sudah benar?")