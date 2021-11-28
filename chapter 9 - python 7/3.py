#membuat function

def FormasiSatu(n):
    for star in range (0,n):
        formasi = '*' *(1+(star-2)*2)
        print(formasi.center(1+2*n))
        
def FormasiDua(n):
    for star in range (0,n):
        formasi = '*' *(n+(star-1)*-2)
        print(formasi.center(1+2*n))
        
def FormasiTiga(n):
        FormasiSatu(n)
        FormasiDua(n)


while True:
    jumlah=int(input('  Masukkan jumlah baris : '))
    if (jumlah%2==1):
        FormasiTiga(jumlah)
        break
    else:
        print('  Bilangan harus ganjil  ')
        Ulang =input('  segera masukkan lagi(y/n)?  ')
        if(Ulang=='y'): 
            continue
        else:
            break