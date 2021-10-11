print("banyak konsumsi BBM")
def bbm(jarak_tempuh,konsumsi_bbm):
    return jarak_tempuh/konsumsi_bbm
#inputdata
jarak_tempuh= float(input("berapa banyak jarak yang di tempuh : "))
konsumsi_bbm= float(input("berapa rata-rata konsumsi BBM perliter : "))
total= bbm(jarak_tempuh, konsumsi_bbm)
print(" jadi, banyak bensin yang dibutuhkan untuk perjalanan yaitu sebanyak", total, "liter")
