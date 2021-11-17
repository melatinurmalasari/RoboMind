veg = ['bayam', 'kangkung', 'wortel', 'selada']

while True:
    print('\nDATA SAYUR')
    A = print('A. Tambahkan data')
    B = print('B. Hapus data')
    C = print('C. Tampilkan data')
    X = print('X. TUTUP')
    pilih = input('Pilih menu: ')
    print('---------------------------------------')    
    while True:
        if(pilih == 'A'):
            insert = str(input('\nTambahkan data baru: '))
            veg.append(insert)
            loop = input('\nAda lagi? (y/n): ')
            if(loop == 'y'):
                continue
            else:
                break
        elif(pilih == 'B'):
            delete = str(input('\nHapus data lama: '))
            x = delete in veg                            
            if(x == True):
                veg.remove(delete)
                loop = input('Hapus data lagi? (y/n): ')
                if(loop == 'y'):
                    continue
                else:
                    break
            elif(x == False):
                print('Data sayur tidak ditemukan')
                loop = input('Ulangi proses? (y/n): ')
                if(loop == 'y'):
                     continue
                else:
                    break
        elif(pilih == 'C'):
             print(veg)
             loop = input('\nMau lihat lagi? (y/n): ')
             if(loop == 'y'):
                 continue
             else:
                 break
        elif(pilih == 'X'):
            break
        else:
            break
    if(pilih == 'X'):
        print('Menutup program.......')
        break
    else:
        break