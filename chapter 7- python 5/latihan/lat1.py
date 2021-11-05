namaFile = str(input("Masukkan nama file: "))
#namaFile = "C:\Users\Melati Nur Malasari\Documents\chapter 7\latihan\contohfile.txt"
try:
    fopen = open(namaFile, "r")
    print(fopen.read())
except FileNotFoundError:
    print("File tidak ditemukan, apakah lokasi file sudah benar")