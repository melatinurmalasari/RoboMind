print("----status kelulusan ujian mahasiswa----")
nama=(input("nama : "))
matematika=float(input("nilai matematika : "))
bahasaindo=float(input("nilai bahasa indonesia : "))
ipa=float(input("nilai IPA : "))
if(matematika>70)and(bahasaindo>60)and(ipa>60):
    print("status kelulusan : ", nama,"dinyatakan LULUS")
else:
    print("status kelulusan : ", nama,"dinyatakan TIDAK LULUS")