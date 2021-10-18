sum=0
total=0
for i in range(100):
    if(i % 2 == 1):
        print(i)
        total+=1
        sum+=i
print('Total bilangan ganjil : ' , total)
print('Jumlah semua bilangan ganjil : ' ,sum)