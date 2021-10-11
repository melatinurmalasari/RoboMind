print("lama waktu perjalanan")
def a_ke_b(jarak_a_ke_b,kecepatan):
    return (jarak_a_ke_b*1000)/(kecepatan*1000/60)
def b_ke_c(jarak_b_ke_c,kecepatan1):
    return (jarak_b_ke_c*1000)/(kecepatan1*1000/60)
def ttl(total,total1,istirahat):
    return (total+total1+istirahat)
#inputdata
jarak_a_ke_b= float(input("berapa jauh jarak dari kota A ke kota B : "))
kecepatan= float(input("berapa kecepatan rata-ratanya : "))
total= round(a_ke_b(jarak_a_ke_b, kecepatan))
print("banyak waktu yang dibutuhkan dari kota A ke kota B", total, "menit")
jarak_b_ke_c= float(input("berapa jauh jarak dari kota A ke kota B : "))
kecepatan1= float(input("berapa kecepatan rata-ratanya : "))
total1= round(b_ke_c(jarak_b_ke_c, kecepatan1))
print("banyak waktu yang dibutuhkan dari kota B ke kota C", total1, "menit")
istirahat= float(input("berapa lama waktu untuk istirahat : "))
ttl0= round(ttl(total,total1,istirahat))
print("total",ttl0, "menit")