print("banyak konsumsi BBM")
def bbm(jarak_tempuh,konsumsi_bbm):
    return jarak_tempuh/konsumsi_bbm
def isi_bbm(total,kapasitas):
    return total/kapasitas
#inputdata
jarak_tempuh= float(input(" jauh jarak yang di tempuh : "))
konsumsi_bbm= float(input("rata-rata konsumsi BBM perliter : "))
total= bbm(jarak_tempuh, konsumsi_bbm)
print("banyak BBM yang di butuhkan", total, "liter")
kapasitas= float(input("kapasitas pengisian tangki BBM : "))
total12= isi_bbm(total, kapasitas)
print(" jadi, berapa banyak pak budi mengisi BBM untuk menyelesaikan perjalanan pak budi", total12, "kali")
