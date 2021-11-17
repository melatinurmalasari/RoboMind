harga_buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def ratarata_harga_buah(x) :
    y=list(x.values())
    v= sum(y)/len(y)
    print("rata-rata harga buaha adalah Rp " , v)

ratarata_harga_buah(harga_buah)