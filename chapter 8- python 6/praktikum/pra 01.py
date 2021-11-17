n = int(input('Masukkan jumlah bilangan yang akan diproses : '))
print('------------------------------------------------')
bil = []
try:
    for i in range(n):
        m = int(input('Masukkan nilai bilangan : '))
        bil.append(m)
    bil.sort()
    bil.reverse()
    print('------------------------------------------------')
    print(bil)
except ValueError:
    print('MAAF TERJADI ERROR :(')