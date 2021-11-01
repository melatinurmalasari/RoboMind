a = int(input('Masukkan bilangan ke-1 : '))
b = int(input('Masukkan bilangan ke-2 : '))
c = int(input('Masukkan bilangan ke-3 : '))

def isPythagoras(a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    else: return False

if(True):
    print("Nilai bilangan : ", (a, b, c), '->', isPythagoras (a, b, c))
else:
    print("Nilai bilangan : ", (a, b, c), '->', isPythagoras (a, b ,c))
