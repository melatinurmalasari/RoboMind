from random import randint
jawaban = randint(0,100)
poin =100
print('           Halo Selamat Datang di Permainan Tebak Angka            ')
print('     disini anda akan ditantang untuk menebak angka dari 0 hingga 100    ')
print('perlu diingat disini pada mulanya anda punya 100 poin dan setiap salah akan berkurang 2')

while True:
    tebakan = input("Masukkan angka : ")
    if (int(tebakan) < jawaban ):
        print('  ')
        print("Terlalu kecil coba dibesarkan lagi angkanya")
        print('poin anda berkurang 2 sekarang tinggal ' + str(poin - 2) )
        print('  ')
        poin -= 2

    if (int(tebakan) > jawaban ):
        print('  ')
        print("Terlalu besar coba dikecilkan lagi angkanya")
        print('poin anda berkurang 2 sekarang tinggal ' + str(poin - 2) )
        print('  ')
        poin -= 2

    if poin == 0 :
        print('kesempatan anda telah habis')
        print('anda tidak dapat menjawab lagi')
        break
    if (int(tebakan) == jawaban ):
        print("-------------------------------------------------------------")
        print("Congratulation!!! anda berhasil menebaknya!!!")
        print("horeee anda berhasil menebaknya")
        break