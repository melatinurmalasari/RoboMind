import time
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}

print('DAFTAR BUAH TERSEDIA            :')
print('-----------------------------------------------')
print(' Harga (/kg)')
print(' Apel   : Rp.5000 \n Jeruk  : Rp.8500 \n Mangga : Rp.7800 \n Duku   : Rp.6500')
print('-----------------------------------------------')

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
        print('Maaf stock buah sedang habis')
    total += bayar
    lagi = str(input('Mau beli buahn yang lain? (y/n): '))

print('-----------------------------------------------')
print('Mohon tunggu (sedang menghitung).......')
time.sleep(3)
print('Harga yang harus anda bayar     : Rp.'+str(total))