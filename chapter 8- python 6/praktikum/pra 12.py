import time
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}

pilih = 'y'

while pilih == 'y':
    print('HALO SELAMAT DATANG :)')
    print('Apa yang ingin anda lakukan?: \nA. Menambahkan Data \nB. Menghapus Data \nC. Beli')
    menu = str(input(' ---> '))
    if menu == 'A':
         nbuah = str(input('Masukkan data baru   : '))
         hbuah = float(input('Masukkan harga (/kg) : '))
         buah[nbuah] = hbuah
         print(buah)
    elif menu == 'C':
        lagi = 'y'
        total = 0
        while lagi == 'y':
            nbuah = input('Buah apa yang ingin anda beli? : ')
            if nbuah in  buah:
                for x,y in buah.items():
                    if(x == nbuah):
                        kg = float(input('Mau beli berapa? (kg)          : '))
                        bayar = kg * y
            else:
                print('MAAF STOCK BUAH SEDANG HABIS :(')
            total += bayar
            lagi = str(input('Mau beli buah yang lain? (y/n): '))

        print('-----------------------------------------------')
        print('Mohon tunggu (sedang menghitung).......')
        time.sleep(3)
        print('Harga yang harus anda bayar     : Rp.'+str(total))
        
    elif menu == 'B':
        Del = str(input('Data yang ingin dihapus : '))
        if Del in buah:
            del buah[Del]
            print(buah)



    print('-----------------------------------------------')
    pilih = str(input('Ingin melakukan transaksi lagi? (y/n) : '))

print('T E R I M A  K A S I H')