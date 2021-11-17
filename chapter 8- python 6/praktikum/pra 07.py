harga_buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def buah_mahal(x) :
    b = dict((v,k) for k,v in x.items())
    c = max(b)
    a = b[c]
    print(a)

buah_mahal(harga_buah)