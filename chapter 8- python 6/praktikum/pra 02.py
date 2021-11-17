def dataStat(x):
    n = 0
    m = 0
    for i in range (len(x)):
        m = m + x[i]
        n += 1
    a = n / m
    b = max(x)
    c = min(x)
    myList = [a,b,c]
    return print(myList)

loop = int(input('Masukkan jumlah bilangan yang ingin diproses : '))
print('--------------------------------------------------')
myList = []
for i in range (loop):
    i += 1
    print('Masukkan bilangan ke-', i,' : ', end="")
    x = int(input())
    myList += [x]
print('--------------------------------------------------')
myTuple = tuple(myList)
dataStat(myTuple)