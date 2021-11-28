def star(n):
    for x in range(n):
        y = "*" + "**"*x
        print(y.center(40," "))


try:
    n= int(input("  Masukkan jumlah Bilanga n : "))
    if n <= 0:
        print("  Ini bukan bilangan asli  ")
except NameError:
    print("  n bukan bilangan bulat  ")
except ValueError:
    print("  n bukan bilangan bulat  ")


star(n)