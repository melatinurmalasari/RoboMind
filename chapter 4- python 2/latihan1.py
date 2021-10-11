print(" rental mobil ")
def jam(jam_keluar, jam_kembali):
    return jam_kembali-jam_keluar
def menit(menit_keluar, menit_kembali):
    return menit_kembali-menit_keluar
def keseluruhan(lamajam, lamamenit):
    return lamajam*60+lamamenit
#inputdata
print(" waktu saat meminjam")
jam_keluar= int(input("jam : "))
menit_keluar= int(input("menit : "))
print(" waktu saat kembali ")
jam_kembali= int(input("jam : "))
menit_kembali=int(input("menit : "))
lamajam= jam(jam_keluar, jam_kembali)
lamamenit= menit(menit_keluar, menit_kembali)
print(" lama pinjam = ",lamajam, "jam",lamamenit, "menit")
total= keseluruhan(lamajam, lamamenit)
if total<721:
    print("harga = Rp 200.000")
elif total>720:
    total= int((total-720)*166.6666666666667+200000)
    print("harga = Rp.", total)
