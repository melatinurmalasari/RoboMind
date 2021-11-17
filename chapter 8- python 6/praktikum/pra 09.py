import time
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}

print('DAFTAR BUAH TERSEDIA            :')
print('-----------------------------------------------')
print(' Apel \n Jeruk \n Mangga \n Duku')
print('-----------------------------------------------')
nbuah = input('Buah apa yang ingin anda beli ? : ')

if nbuah in  buah:
    for x,y in buah.items():
        if(x == nbuah):
            kg = float(input('Mau beli berapa? (kg)           : '))
            bayar = kg * y
            print('-----------------------------------------------')
            print('Mohon tunggu (sedang menghitung).......')
            time.sleep(3)
            print('Harga yang harus anda bayar     : Rp.'+str(bayar))
else:
    print('Maaf stock buah sedang habis')