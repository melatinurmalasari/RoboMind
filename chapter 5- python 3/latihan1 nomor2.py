print("----status kelulusan ujian mahasiswa----")
nama=(input("nama : "))
matematika=float(input("nilai matematika : "))
bahasaindo=float(input("nilai bahasa indonesia : "))
ipa=float(input("nilai IPA : "))
if(matematika<0)or(bahasaindo<0)or(ipa<0)or(matematika>100)or(bahasaindo>100)or(ipa>100):
    print(" maaf input yang ada yang tidak valid")
elif(matematika>70)and(bahasaindo>60)and(ipa>60):
    print("status kelulusan :", nama, "dinyatakan LULUS")
else:
    print(" status kelulusan :", nama, "dinyatakan TIDAK LULUS")

