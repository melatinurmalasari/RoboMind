print("----------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("----------------------------")

lagi = 'Yes'
total = 0
n = 0

while True:
    try:
        bil = int(input("Masukkan nilai bilangan bulat            : "))
        
    except ValueError:
        print("Maaf angka yang anda masukkan bukan bilangan bulat")
        continue

    total += bil
    n += 1
    lagi = input("Tambah lagi? (Yes/No)                           : ")
    if (lagi == "Yes"):
        continue
    else:
         break

hasil = total/n
print("\nRata-rata data dari nilai yang anda masukkan adalah : ", hasil)