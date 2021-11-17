# Langkah Kerja 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)


# Langkah Kerja 2
a.insert(2,10)
b.insert(1,15)
print('\n')
print(a)
print(b)


# Langkah Kerja 3
a.append(4)
b.append(8)
print('\n')
print(a)
print(b)


# Langkah Kerja 4
a.sort()
b.sort()
print('\n')
print(a)
print(b)


# Langkah Kerja 5
c = a[:8]
d = b[2:10]
print('\n')
print(c)
print(d)
print('\n')


# Langkah Kerja 6
e = []
for num in range(len(c)):
    e += [c[num]+d[num]]
print(e)


# Langkah Kerja 7
e = tuple(e)
print('\n')
print(e)


# Langkah Kerja 8
print('\n')
print(max(e))
print(min(e))
print(sum(e))
print('\n')


# Langkah Kerja 9
myString = "Python adalah bahasa pemrograman yang menyenangkan"


# Langkah Kerja 10
myString = set(myString)
print(myString)
print('\n')


# Langkah Kerja 11
myString = list(myString)
myString.sort()
print(myString)