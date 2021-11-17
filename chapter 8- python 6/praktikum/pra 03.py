msis = []
lagi = 'y'
nama = []

try:
    while lagi == 'y':
        nama = str(input('Masukkan nama mahasiswa : '))
        msis.append(nama)
        lagi = str(input('Lagi ? (y/n) : '))

    print('---------------------------------------------')

    msis.sort()
    count = [len(a) for a in msis]
    n = 0
    for i in range(len(msis)):
        print(msis[i], '(',str(count[n]), 'karakter )')
        n += 1

except ValueError:
    print('Error 404 :(')