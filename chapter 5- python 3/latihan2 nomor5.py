from random import randint
jawaban = randint(0,100)

print('              halo selamat datang di permainan tebak angka          ')
print('      disini anda akan ditantang untuk menebak angka dari 0 hingga 100      ')

while True:
    tebakan = input("Masukkan angka : ")
    if (int(tebakan) < jawaban ):
        print('  ')
        print("Terlalu kecil coba dibesarkan lagi angkanya")
        print('  ')
    if (int(tebakan) > jawaban ):
        print('  ')
        print("Terlalu besar coba dikecilkan lagi angkanya")
        print('  ')
    if (int(tebakan) == jawaban ):
        print("------------------------------------------------------------")
        print("Congratulation!!! anda berhasil menebaknya!!!")
        print("Horee anda telah berhasil menebaknya")
        break